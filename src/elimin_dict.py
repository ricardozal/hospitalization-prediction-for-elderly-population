elimin_A = {
    'Person Specific Identifier', # Person Specific Identifier  (MANDATORY)
    'Household Identifier', # Household Identifier (MANDATORY) 
    'Spouse Identifier', # Spouse Identifier (MANDATORY)   
    'Response Indicator', # Wave Status: Response Indicator (MANDATORY)   
    # 'Interview Status', # Wave Status: Interview Status  
    'Sample Cohort', # Sample Cohort  
    'Whether Proxy Interview', # Whether Proxy Interview  
    # 'Number of Household Respondents', # Number of Household Respondents  
    # 'Whether Couple Household', # Whether Couple Household  
    'Household Analysis Weight', # Household Analysis Weight (MANDATORY)  
    'Person-Level Analysis Weight', # Person-Level Analysis Weight
    # 'Interview Dates', # Interview Dates  
    # 'Birth Date', # Birth Date: Month and Year  
    'Death Date', # Death Date: Month and Year  
    # 'Age at Interview', # Age at Interview (Months and Years)  
    # 'Gender', # Gender  
    # 'Education', # Education  
    # 'Education_Cat', # Education: Categories by ISCED Codes  
    # 'Education_ Harmon', # Education: Harmonized Education  
    'Literacy and Numeracy', # Literacy and Numeracy  
    # 'Indigenous Language', # Indigenous Language  
    # 'Current Partnership Status', # Current Marital Status: Current Partnership Status  
    # 'With Partnership', # Current Marital Status: With Partnership  
    # 'Without Partnership', # Current Marital Status: Without Partnership  
    # 'Number of Marriages', # Number of Marriages  
    # 'Urban or Rural' # Urban or Rural
}

elimin_B = {
    # 'Self-Report of Health',  # Self-Report of Health  
    # 'ADLs Raw Recodes',  # Activities of Daily Living (ADLs): Raw Recodes  
    # 'ADLs Some Difficulty',  # Activities of Daily Living (ADLs): Some Difficulty 
    # 'IADLs Raw Recodes',  # Instrumental Activities of Daily Living (IADLs): Raw Recodes  
    # 'IADLs Some Difficulty',  # Instrumental Activities of Daily Living (IADLs): Some Difficulty  
    # 'Other Limitations Raw Recodes',  # Other Functional Limitations: Raw Recodes  
    # 'Other Limitations Some Difficulty',  # Other Functional Limitations: Some Difficulty  
    'ADL Summary',  # ADL Summary: Sum ADLs Where Respondent Reports Any Difficulty  
    'IADL Summary',  # IADL Summary: Sum IADLs Where Respondent Reports Any Difficulty  
    # 'Other Summary Indices',  # Other Summary Indices: Mobility, Large Muscle, Gross, Fine Motor, Total, Upper, Lower Body Mobility, and NAGI Activities 
    # 'Doctor Diagnosed Health Problems',  # Doctor Diagnosed Health Problems: Ever Have Condition  
    # 'Treatment or Medication for Disease',  # Doctor Diagnosed Diseases: Whether Receives Treatment or Medication for Disease  
    # 'Whether Disease Limits Activity',  # Doctor Diagnosed Diseases: Whether Disease Limits Activity  
    # 'Age of Diagnosis',  # Doctor Diagnosed Diseases: Age of Diagnosis  
    # 'Vision',  # Vision  
    # 'Hearing',  # Hearing 
    # 'Falls',  # Falls  
    # 'Urinary Incontinence',  # Urinary Incontinence  
    # 'Persistent Health Problems',  # Persistent Health Problems  
    'Sleep',  # Sleep  
    # 'Pain',  # Pain  
    'Menopause',  # Menopause  
    # 'BMI',  # BMI  
    # 'Physical Activity or Exercise',  # Health Behaviors: Physical Activity or Exercise  
    # 'Drinking',  # Health Behaviors: Drinking  
    # 'Smoking (Cigarettes)',  # Health Behaviors: Smoking (Cigarettes)  
    'Preventive Care',  # Health Behaviors: Preventive Care
}

elimin_C = {
    # 'Medical Care Hospital',  # Medical Care Utilization: Hospital  
    # 'Medical Care Doctor',  # Medical Care Utilization: Doctor  
    # 'Medical Care Other',  # Medical Care Utilization: Other Medical Care Utilization  
    'Medical Expenditures',  # Medical Expenditures: Out of Pocket and Total  
    'Covered by Government',  # Covered by Federal Government Health Insurance Program  
    'Covered by Private',  # Covered by Private Health Insurance  
    'Covered by Employer',  # Covered by Health Insurance from a Current or Previous Employer  
    # 'Number of Health Insurance Plans',  # Number of Health Insurance Plans
}

elimin_D = {
    # 'Cognition Testing Conditions',  # Cognition Testing Conditions 
    # 'Self-Reported Memory',  # Self-Reported Memory 
    # 'Immediate Word Recall',  # Immediate Word Recall 
    # 'Delayed Word Recall',  # Delayed Word Recall 
    # 'Summary Scores',  # Summary Scores 
    # 'Picture Drawing',  # Picture Drawing 
    # 'Verbal Fluency',  # Verbal Fluency 
    # 'Visual Scanning',  # Visual Scanning 
    # 'Backwards Counting From 20',  # Backwards Counting From 20 
    'Date Naming/Orientation',  # Date Naming/Orientation 
    # 'Serial 7s',  # Serial 7’s -> 'Serial 7s'
    'JORM IQCODE',  # Proxy Cognition: JORM IQCODE 
    # 'Ratings of Memory and Abilities',  # Proxy Cognition: Ratings of Memory and Abilities 
    # 'Cognitive Impairment',  # Proxy Cognition: Cognitive Impairment 
    # 'Problem Behaviors in Past Week',  # Proxy Cognition: Problem Behaviors in Past Week
}  

elimin_E = {
    'Inflation Multiplier',  # Inflation Multiplier (MANDATORY)
    'Net Value of Real Estate',  # Net Value of Real Estate (Not Primary Residence) 
    'Net Value of Cars',  # Net Value of Cars 
    'Net Value of Businesses',  # Net Value of Businesses 
    'Value of Stocks',  # Value of Stocks Shares and Bonds 
    'Value of Accounts',  # Value of Checking Savings Accounts 
    'Value of Other',  # Value of Other Assets
    'Value of Residence',  # Value of Primary Residence 
    'Value of Mortgages',  # Value of All Mortgages (Primary Residence)
    'Net Value P Residence',  # Net Value of Primary Residence
    'Home ownership',  # Home ownership
    'Value of Other Debt',  # Value of Other Debt
    'Value of Loans Lent',  # Value of Loans Lent
    'Net Value Financial Wealth',  # Net Value of Non-Housing Financial Wealth (Excluding IRAs)
    # 'Total Wealth',  # Total Wealth
}   

elimin_F = {
    'Individual Earnings',  # Individual Earnings
    'Household Income',  # Household Capital Income
    'Income from Private Pension',  # Individual Income from Private Pension
    'Public Pension Income',  # Individual Public Pension Incomes
    'Other Pensions Income',  # Individual Other Pensions Income
    'Total Pensions Income',  # Individual Total Pensions Income
    'Other Government Transfers',  # Individual Income from Other Government Transfers
    'All Other Income',  # All Other Income
    # 'Total Household Income r&s',  # Total Household Income (respondent & spouse)
    # 'Total Household Consumption h',  # Total Household Consumption (full household)
}

elimin_G = {
    # 'N Living in Household',  # Number of People Living in Household
    # 'N Living Children',  # Number of Living Children
    # 'N Deceased Children',  # Number of Deceased Children
    # 'N Children Ever Born',  # Number of Children Ever Born
    # 'N Grandchildren',  # Number of Grandchildren
    # 'N Living Siblings',  # Number of Living Siblings
    # 'N Deceased Siblings',  # Number of Deceased Siblings
    # 'N Living Parents',  # Number of Living Parents
    # 'Parental Mortality',  # Parental Mortality
    # 'Parents Age or Age at Death',  # Parents' Current Age or Age at Death
    # 'Parents Education',  # Parents' Education
    # 'Any Child with Respondent',  # Any Child Co-Resides with Respondent
    # 'Any Children Same City',  # Any Children Living in the Same City
    # 'Any Weekly Contact with Children',  # Any Weekly Contact with Children
    # 'Frequent Contact with Relatives',  # Frequent or Weekly Contact with Relatives and Friends
    'Weekly Social Activities',  # Any Weekly Social Activities or Participate in Religious Groups
    # 'Financial Transfer from Children',  # Financial Transfer from Children
    # 'Financial Transfer to Children',  # Financial Transfer to Children
    # 'Financial Transfer to Parents',  # Financial Transfer to Parents
}

elimin_H = {
    'Currently Working for Pay',  # Currently Working for Pay
    'Whether Self-Employed',  # Whether Self-Employed
    'Labor Force Status',  # Labor Force Status
    'In the Labor Force',  # In the Labor Force
    # 'Unemployment Status',  # Unemployment Status
    'Retired Employment Status',  # Retired Employment Status
    'Hours at Main Job',  # Hours at Main Job
    'Main Activity Years of Tenure',  # Main Activity Years of Tenure
    'Job Allows Move',  # Job Allows Move to Less Demanding Work
    'Occupation Code with Longest',  # Occupation Code for Job with Longest Reported Tenure
    # 'Year Last Job Ended',  # Year Last Job Ended
    # 'Reason Job Ended',  # Reason Job Ended
}

elimin_I = {
    'Retirement year',  # Whether Retired: Retirement year, if says retired
    # 'Retirement age',  # Whether Retired: Retirement age, if says retired
}

elimin_J = {
    'Public Pension',  # Whether Receives Public Pension
    'Private Pension',  # Whether Receives Private Pension
    'Other Pension',  # Whether Receives Other Pension
    'Age Public Pension',  # Age When Started to Receive a Public Pension
    'Age Private Pension',  # Age When Started to Receive a Private Pension
    'Public Pension Continuity',  # Whether Current Public Pension(s) Can Continue
    'Private Pension Continuity',  # Whether Current Private Pension Can Continue
}

elimin_K = {
    # 'Waist and Hip Measure',  # Height, Weight, Waist and Hip Circumference Measurements
    # 'Waist and Hip Measure Incomplete',  # Height, Weight, Waist and Hip Circumference Measurements: Reason Didn't Complete
    'Sitting Height',  # Sitting Height
    'Sitting Height Incomplete',  # Sitting Height: Reason Didn't Complete
    # 'Balance Test',  # Balance Test
    # 'Balance Test Incomplete',  # Balance Test: Reason Didn't Complete
    'Blood Pressure Measure',  # Blood Pressure Measurements
    'Blood Pressure Measure Incomplete',  # Blood Pressure Measurements: Reason Didn't Complete
    'Timed Walk Measure',  # Timed Walk Measurements
    'Timed Walk Measure Incomplete',  # Timed Walk Measurements: Reason Didn't Complete
    'Hand Grip Measure',  # Hand Grip Strength Measurements
    'Hand Grip Measure Incomplete',  # Hand Grip Strength Measurements: Reason Didn't Complete
}

elimin_L = {
    # 'ADL Help',  # ADL Help
    # 'IADL Help',  # IADL Help
    # 'Personal Aids',  # Whether Uses Personal Aids
    # 'Future ADL Help',  # Future ADL Help
    # 'ADL Any Care',  # Activities of Daily Living: Whether Receives Any Care
    # 'ADL Informal Care',  # Activities of Daily Living: Whether Receives Any Informal Care
    # 'ADL Informal Care Spouse',  # Activities of Daily Living: Receives Informal Care from Spouse
    # 'ADL Care Children or Grandchildren',  # Activities of Daily Living: Receives Informal Care from Children or Grandchildren
    # 'ADL Care Relatives',  # Activities of Daily Living: Receives Informal Care from Relatives
    # 'ADL Care Other Individuals',  # Activities of Daily Living: Receives Informal Care from Other Individuals
    # 'ADL Formal Care',  # Activities of Daily Living: Whether Receives Any Formal Care
    # 'ADL Care Paid Professional',  # Activities of Daily Living: Receives Formal Care from Paid Professional
    # 'IADL Any Care',  # Instrumental Activities of Daily Living: Whether Receives Any Care
    # 'IADL Informal Care',  # Instrumental Activities of Daily Living: Whether Receives Any Informal Care
    # 'IADL Informal Care Spouse',  # Instrumental Activities of Daily Living: Receives Informal Care from Spouse
    # 'IADL Care Children or Grandchildren',  # Instrumental Activities of Daily Living: Receives Informal Care from Children or Grandchildren
    # 'IADL Care Relatives',  # Instrumental Activities of Daily Living: Receives Informal Care from Relatives
    # 'IADL Care Other Individuals',  # Instrumental Activities of Daily Living: Receives Informal Care from Other Individuals
    # 'IADL Formal Care',  # Instrumental Activities of Daily Living: Whether Receives Any Formal Care
    # 'IADL Care Paid Professional',  # Instrumental Activities of Daily Living: Receives Formal Care from Paid Professional
    # 'ADL & IADL Any Care',  # Activities of Daily Living and Instrumental Activities of Daily Living: Whether Receives Any Care
    # 'ADL & IADL Informal Care',  # Activities of Daily Living and Instrumental Activities of Daily Living: Whether Receives Any Informal Care
    # 'ADL & IADL Care Spouse',  # Activities of Daily Living and Instrumental Activities of Daily Living: Receives Informal Care from Spouse
    # 'ADL & IADL Care Children or Grandchildren',  # Activities of Daily Living and Instrumental Activities of Daily Living: Receives Informal Care from Children or Grandchildren
    # 'ADL & IADL Care Relatives',  # Activities of Daily Living and Instrumental Activities of Daily Living: Receives Informal Care from Relatives
    # 'ADL & IADL Care Other Individuals',  # Activities of Daily Living and Instrumental Activities of Daily Living: Receives Informal Care from Other Individuals
    # 'ADL & IADL Formal Care',  # Activities of Daily Living and Instrumental Activities of Daily Living: Whether Receives Any Formal Care
    # 'ADL & IADL Care Paid Professional',  # Activities of Daily Living and Instrumental Activities of Daily Living: Receives Formal Care from Paid Professional
    # 'Help Children or Grandchildren',  # Receives Help with Chores from Children or Grandchildren
    # 'Provides Care to Children or Grandchildren',  # Provides Informal Care to Children or Grandchildren
    # 'Provides Care to Parents',  # Provides Personal Care to Parents
    # 'Provides Care for Sick or Disabled Adults',  # Provides Informal Care for Sick or Disabled Adults
}

elimin_M = {
    # 'Support Spouse',  # Social Support: Spouse
    # 'Support Children',  # Social Support: Children
    # 'Support: Friends',  # Social Support: Friends
    # 'Experienced Death of a Child',  # Experienced Death of a Child
}

elimin_O = {
    'Has a Will',  # Will: Whether Has a Will
    'Beneficiaries Will',  # Will: Beneficiaries of Will
    'Covered Life Insurance',  # Covered by Life Insurance
}

elimin_Q = {
    # 'Depressive Symptoms',  # Depressive Symptoms: CESD
    # 'Satisfaction Life',  # Satisfaction with Life Scale
    # 'Single Life Satisfaction',  # Single Life Satisfaction Question
    'Cantril Ladder',  # Cantril Ladder
}

