import pandas as pd
import glob

# get all CSV files in the directory
files = glob.glob("*.csv")

# create an empty dataframe
df = pd.DataFrame()

# loop through each CSV file and concatenate them
for file in files:
    temp_df = pd.read_csv(file)
    df = pd.concat([df, temp_df], axis=0)

# write the final merged data into a new CSV file
df.to_csv("merged_data.csv", index=False)