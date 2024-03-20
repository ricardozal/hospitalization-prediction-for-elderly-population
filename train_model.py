from collections import Counter
import os

from imblearn.over_sampling import SMOTE
from lightgbm import LGBMClassifier
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, make_scorer
from sklearn.model_selection import RandomizedSearchCV, train_test_split

from src import config, data_utils, data_eda, preprocessing, constants


"""
    - Get raw dataset
"""
h_mhas_c2 = data_utils.get_datasets()

print(f"Dataset path: {os.path.join(config.DATASET_ROOT_PATH, config.DATASET_MHAS_C2)}")
print(f"Rows: {h_mhas_c2.shape[0]}")
print(f"Columns: {h_mhas_c2.shape[1]}")

"""
    - Data cleaning and transformation
"""

# After a subjective discussion, it was determined that for the `Hospitalization Prediction for Elderly Population`
# project, we would not need the following subsections
h_mhas_c2 = data_utils.remove_unnecessary_columns(h_mhas_c2, constants.EXCLUDED_SUBSECTIONS)

print(f"Columns after removing excluded subsections")
print(f"Columns: {h_mhas_c2.shape[1]}")

# Dataframe transformation
h_mhas_c2 = data_utils.concat_waves(h_mhas_c2)

print(f"Columns and rows after transforming")
print(f"Rows: {h_mhas_c2.shape[0]}")
print(f"Columns: {h_mhas_c2.shape[1]}")

# Identify the variable named 'hosp1y' and rename it to 'TARGET'
h_mhas_c2.rename(columns={constants.ORIGINAL_TARGET_NAME: 'TARGET'}, inplace=True)

# Delete all rows where the variable 'TARGET' is equal to null
h_mhas_c2.dropna(subset=['TARGET'], inplace=True)

print(f"Rows after removing all rows where the variable 'TARGET' is equal to null")
print(f"Rows: {h_mhas_c2.shape[0]}")

# Remove other useless features
h_mhas_c2.drop(columns=[constants.USELESS_FEATURES], inplace=True)

# Remove columns where the percentage of null values is higher than 30%
# Calculate the percentage of missing values for each column
total_values = h_mhas_c2.isnull().sum()
missing_percentage = round((total_values / len(h_mhas_c2)) * 100, 1)

# Identify columns where the percentage of missing values is greater than 30%
columns_with_missing_values_to_drop = missing_percentage[missing_percentage > 30].index

# Drop these columns from the DataFrame
h_mhas_c2.drop(columns=columns_with_missing_values_to_drop, inplace=True)

print(f"Columns and rows after removing columns where the percentage of null values is higher than 30%")
print(f"Rows: {h_mhas_c2.shape[0]}")
print(f"Columns: {h_mhas_c2.shape[1]}")

# Some features have a high correlation, so our next step is to identify these variables and then eliminate them.
h_mhas_c2 = data_eda.elim_bycorr(h_mhas_c2, 0.9)

# Finally, we verify that we do not have features that are highly correlated with the target variable.
h_mhas_c2 = data_eda.remove_highly_correlated(h_mhas_c2, 'TARGET', 0.9)

print(f"Columns and rows after removing columns are highly correlated")
print(f"Rows: {h_mhas_c2.shape[0]}")
print(f"Columns: {h_mhas_c2.shape[1]}")

# Save dataset for training
h_mhas_c2.to_csv(config.DATASET_TRAIN, index=False)

del h_mhas_c2


"""
    - Get dataset for training
"""
df_train = data_utils.get_datatrain()


""" 
    - Preprocessing
"""

# Separate target feature
X_train = df_train.drop(columns="TARGET", axis=1)
y_train = df_train["TARGET"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# 3.2 Applying SimpleImputer and Scale data using pipeline
preprocessing.get_transform_pipeline(X_train)

X_train = preprocessing.preprocess_dataframe(X_train)
X_test = preprocessing.preprocess_dataframe(X_test)

# Apply SMOTE to address a class imbalance (1 variable) in a dataset
sm = SMOTE(sampling_strategy='minority', random_state=42)

# fit predictor and target variable
old_y_train = y_train
X_train, y_train = sm.fit_resample(X_train, y_train)

print('Original dataset shape', Counter(old_y_train))
print('Resample dataset shape', Counter(y_train))


"""## 4. Train LightGBM model"""

# Initialize a LightGBM Classifier with 'auc' as the evaluation metric
lgbm_model = LGBMClassifier(metric='auc')
lgbm_model.fit(X_train, y_train)

# Train data predictions (class 1)
pred_train = lgbm_model.predict_proba(X_train)[:, 1]

# Validation data predictions (class 1)
pred_val = lgbm_model.predict_proba(X_test)[:, 1]

# Train ROC AUC Score
roc_auc_train = roc_auc_score(y_true=y_train, y_score=pred_train)
print(f"Train ROC AUC Score for LightGBM model: {roc_auc_train:.4f}")

# Validation ROC AUC Score
roc_auc_val = roc_auc_score(y_true=y_test, y_score=pred_val)
print(f"Validation ROC AUC Score for LightGBM model: {roc_auc_val:.4f}")

y_pred = lgbm_model.predict(X_test)

print("--- CLASSIFICATION REPORT FOR LightGBM MODEL ---")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

print("--- CONFUSION MATRIX FOR LightGBM MODEL ---")
print(cm)

"""## 5. Train Random Forest model using RandomizedSearchCV with the top 50 most important features from trained LGBM"""

number_of_used_features = 50

start_index = max(len(X_train.columns) - number_of_used_features, 0)

sorted_idx = lgbm_model.feature_importances_.argsort()
top50_features = X_train.columns[sorted_idx][:-number_of_used_features-1:-1]

print("--- top 50 most important features from trained LGBM ---")
print(top50_features.tolist())

param_dist = {
    "max_depth": [3, 5, None],
    "max_features": [0.2, 0.6, 1.0],
    "min_samples_split": [2, 5],
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
    "n_estimators": [20, 60, 100],
    "min_samples_leaf": [1, 2]
}

roc_auc_scorer = make_scorer(roc_auc_score)

rf = RandomForestClassifier()
model = RandomizedSearchCV(rf, param_distributions=param_dist, cv=5, scoring=roc_auc_scorer, verbose=2, n_jobs=-1)
model.fit(X_train[top50_features.tolist()], y_train)

# Train data predictions (class 1)
rf_pred_train = model.predict_proba(X_train[top50_features.tolist()])[:, 1]

# Validation data predictions (class 1)
rf_pred_val = model.predict_proba(X_test[top50_features.tolist()])[:, 1]

# Train ROC AUC Score
roc_auc_train = roc_auc_score(y_true=y_train, y_score=rf_pred_train)
print(f"Train ROC AUC Score for Random Forest: {roc_auc_train:.4f}")

# Validation ROC AUC Score
roc_auc_val = roc_auc_score(y_true=y_test, y_score=rf_pred_val)
print(f"Validation ROC AUC Score for Random Forest: {roc_auc_val:.4f}")

y_pred = model.predict(X_test[top50_features.tolist()])

print("--- CLASSIFICATION REPORT FOR RANDOM FOREST MODEL ---")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

print("--- CONFUSION MATRIX FOR RANDOM FOREST MODEL ---")
print(cm)

# Save the model to a file
joblib.dump(model, constants.FINAL_MODEL)
