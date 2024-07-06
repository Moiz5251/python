import pandas as pd
import os

# Get a list of all XLSX files in the directory
files = [f for f in os.listdir('.') if f.endswith('.xlsx')]

# Create an empty DataFrame to hold the merged data
merged_df = pd.DataFrame()

# Loop through each XLSX file
for file in files:
    # Read the Excel file
    xls = pd.read_excel(file, sheet_name=None)

    # Loop through each sheet and concatenate to the merged DataFrame
    for sheet_name, df in xls.items():
        # Skip the first row of each sheet and concatenate to the merged DataFrame
        merged_df = pd.concat([merged_df, df.iloc[1:]], ignore_index=True, sort=False)

# Save the merged DataFrame to a new XLSX file
merged_df.to_excel('merged.xlsx', index=False)
