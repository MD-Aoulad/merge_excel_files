import pandas as pd
import os

# Specify the directory containing the input files. Please use "/" instead of "\". It took me quite some time to find the issue.
input_dir = '/path/to/input/directory/'

# Get a list of all files in the directory
files = os.listdir(input_dir)

# Initialize an empty list to store the dataframes
dfs = []

# Loop through each file in the directory
for file in files:
    # Check if the file is an Excel file
    if file.endswith('.xlsx'):
        # Read the Excel file as a dataframe and append it to the list
        df = pd.read_excel(input_dir + file)
        dfs.append(df)

# Specify the path and filename of the output file
output_file = '/path/to/output/file/merged_excel_file.xlsx'

# Concatenate all dataframes into a single dataframe
merged_df = pd.concat(dfs)

# Write the merged dataframe to an Excel file
merged_df.to_excel(output_file, index=False)

# Print a message indicating that the file has been created and its location
print("Merged file created at:", output_file)
