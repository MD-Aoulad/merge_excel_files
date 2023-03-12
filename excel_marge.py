import pandas as pd
import os

path = 'C:/Users/ekra5/Desktop/python/test python project/amazon/'

files = os.listdir(path)
dfs = []
for file in files:
    if file.endswith('.xlsx'):
        df = pd.read_excel(path + file)
        dfs.append(df)

output_file = 'C:/Users/ekra5/Desktop/python/test python project/amazon/merged_excel_file.xlsx'
merged_df = pd.concat(dfs)
merged_df.to_excel(output_file, index=False)
print("File created at:", output_file)
