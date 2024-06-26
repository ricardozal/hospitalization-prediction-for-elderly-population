import json
import os

EXCLUDED_SUBSECTIONS = ['Person Specific Identifier', 'Household Identifier', 'Spouse Identifier',
                              'Response Indicator', 'Sample Cohort', 'Whether Proxy Interview',
                              'Household Analysis Weight', 'Person-Level Analysis Weight', 'Death Date',
                              'Literacy and Numeracy', 'ADL Summary', 'IADL Summary', 'Sleep', 'Menopause',
                              'Preventive Care', 'Medical Expenditures', 'Covered by Government', 'Covered by Private',
                              'Covered by Employer', 'Date Naming/Orientation', 'JORM IQCODE', 'Inflation Multiplier',
                              'Net Value of Real Estate', 'Net Value of Cars', 'Net Value of Businesses',
                              'Value of Stocks', 'Value of Accounts', 'Value of Other', 'Value of Residence',
                              'Value of Mortgages', 'Net Value P Residence', 'Home ownership', 'Value of Other Debt',
                              'Value of Loans Lent', 'Net Value Financial Wealth', 'Individual Earnings',
                              'Household Income', 'Income from Private Pension', 'Public Pension Income',
                              'Other Pensions Income', 'Total Pensions Income', 'Other Government Transfers',
                              'All Other Income', 'Weekly Social Activities', 'Currently Working for Pay',
                              'Whether Self-Employed', 'Labor Force Status', 'In the Labor Force',
                              'Retired Employment Status', 'Hours at Main Job', 'Main Activity Years of Tenure',
                              'Job Allows Move', 'Occupation Code with Longest', 'Retirement year', 'Public Pension',
                              'Private Pension', 'Other Pension', 'Age Public Pension', 'Age Private Pension',
                              'Public Pension Continuity', 'Private Pension Continuity', 'Sitting Height',
                              'Sitting Height Incomplete', 'Blood Pressure Measure', 'Blood Pressure Measure Incomplete',
                              'Timed Walk Measure', 'Timed Walk Measure Incomplete', 'Hand Grip Measure',
                              'Hand Grip Measure Incomplete', 'Has a Will', 'Beneficiaries Will',
                              'Covered Life Insurance', 'Cantril Ladder']

USELESS_FEATURES = ['rabyear', 'rabmonth', 'iwy', 'iwm', 'hspnit1y', 'doctim1y', 'momage', 'dadage']

ORIGINAL_TARGET_NAME = 'hosp1y'

FINAL_MODEL = 'final_model.pkl'
