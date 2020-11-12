import pandas as pd

read_file = pd.read_excel (r'C:\Users\UMA\OneDrive\Desktop\chennai to toronto comparison.xlsx', sheet_name='Sheet1')
read_file.to_csv (r'C:\Users\UMA\OneDrive\Desktop\citiescomparison.csv', index = None, header=True)
