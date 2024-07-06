import pandas as pd
import os

# Get a list of all XLSX files in the directory
files = [f for f in os.listdir('.') if f.endswith('.xlsx')]

# Loop through each XLSX file
for file in files:
    # Read the Excel file
    xls = pd.read_excel(file, sheet_name=None)

    # Loop through each sheet and save as a separate XLSX file
    for sheet_name, df in xls.items():
        # Save the sheet as an XLSX file with the original file name appended to the sheet name
        df.to_excel(f'{file}_{sheet_name}.xlsx', index=False)

    # Delete the original file
    os.remove(file)
