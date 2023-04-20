import pandas as pd

# Load the Excel file into a pandas DataFrame
df = pd.read_excel("DCP_Requirement_Coverage-04-19-2023_Sample.xlsx", sheet_name="DCP Requirement Coverage")

# Split the comma-separated values in the "ColumnA" column into separate rows
df = df.assign(ColumnA=df["ColumnA"].str.split(",")).explode("ColumnA")

# Save the modified DataFrame back to the Excel file
df.to_excel("file.xlsx", sheet_name="Sheet1", index=False)
