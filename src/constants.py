import json
import os

UNNECESARY_SECTION_COLUMNS = [
    "Person Specific Identifier", "Household Identifier",
    "Spouse Identifier", "Response Indicator", "Sample Cohort",
    "Whether Proxy Interview", "Household Analysis Weight",
    "Person-Level Analysis Weight", "Death Date", "Literacy and Numeracy",
    "Preventive Care", "IADL Summary", "Menopause", "Sleep", "ADL Summary",
    "Covered by Employer", "Covered by Private", "Medical Expenditures",
    "Covered by Government", "JORM IQCODE", "Date Naming/Orientation",
    "Inflation Multiplier", "Net Value of Cars", "Value of Loans Lent",
    "Net Value Financial Wealth", "Home ownership", "Net Value P Residence",
    "Value of Other Debt", "Value of Accounts", "Net Value of Businesses",
    "Net Value of Real Estate", "Value of Mortgages", "Value of Other",
    "Value of Residence", "Value of Stocks", "Public Pension Income",
    "Household Income", "Income from Private Pension",
    "Other Pensions Income", "Individual Earnings",
    "Total Pensions Income", "All Other Income",
    "Other Government Transfers", "Weekly Social Activities",
    "Whether Self-Employed", "Main Activity Years of Tenure",
    "In the Labor Force", "Hours at Main Job", "Job Allows Move",
    "Retired Employment Status", "Labor Force Status",
    "Currently Working for Pay", "Occupation Code with Longest",
    "Retirement year", "Private Pension", "Age Private Pension",
    "Public Pension Continuity", "Private Pension Continuity",
    "Age Public Pension", "Public Pension", "Other Pension",
    "Timed Walk Measure Incomplete", "Timed Walk Measure",
    "Sitting Height Incomplete", "Sitting Height", "Hand Grip Measure",
    "Blood Pressure Measure Incomplete", "Blood Pressure Measure",
    "Hand Grip Measure Incomplete", "Beneficiaries Will",
    "Covered Life Insurance", "Has a Will", "Cantril Ladder"
]

USED_VARIABLES = [
    'hltc', 'agey', 'height', 'decsib', 'henum', 'doctor1y', 'bmi', 'weight', 'cagem', 'outpt1y', 'fallinj',
    'mstat', 'livsib', 'shlt', 'imrc8', 'sight', 'mrct', 'drink', 'hearing', 'vscan', 'smokev', 'rxdiabi',
    'tr16', 'swell', 'hrtatte', 'fallnum', 'mstath', 'dentim1y', 'rxhibp', 'respe', 'rxarthr', 'painlv',
    'cancre', 'ftired', 'glasses', 'diabe', 'joga', 'shop', 'fatigue', 'vigact', 'rxhrtat', 'cesd_m', 'dlrc8',
    'fall', 'rxresp', 'push', 'nagi10', 'hearaid', 'breath_m', 'sleepr'
]

with open(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "model_variables.json")
) as model_variables_file:
    JSON_MODEL_VARIABLES = json.load(model_variables_file)
    MODEL_VARIABLES = {
        variable: JSON_MODEL_VARIABLES[variable]
        for variable in USED_VARIABLES
    }
