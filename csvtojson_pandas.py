#Convert CSV to JSON
import pandas as pd
df = pd.read_csv (r'C:\Users\UMA\OneDrive\Desktop\Amazon\annual-enterprise-survey-2019-financial-year-provisional-csv.csv')
df.to_json (r'C:\Users\UMA\OneDrive\Desktop\Amazon\enterprisesurvey.json')
print(df)


