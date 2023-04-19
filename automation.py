import pandas as pd

# Read in Excel file
df = pd.read_excel('my_excel_file.xlsx')

# Group by Requirement column and sum other columns
df = df.groupby('Requirement').sum().reset_index()

# Drop duplicates in Requirement column
df.drop_duplicates(subset='Requirement', keep = 'first', inplace = True)

# Print resulting dataframe
print(df)