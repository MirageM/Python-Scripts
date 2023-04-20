import csv

# Specify the input and output file names
input_file = "Sample.csv"
output_file = "my_excel_file.csv"

# Specify the column that contains the values to separate
column_to_split = 1 # Replace with the index of your desired column, starting from 0

# Open the input and output files

with open(input_file, 'r', encoding='ISO-8859-1') as csv_file, open(output_file, 'w', newline='') as output:
    reader = csv.reader(csv_file)
    writer = csv.writer(output)

    # Loop through each row in the input file
    for row in reader:
        # Split the value in the specified column by comma
        values = row[column_to_split].split(',')

        # Loop through each value and write a new row to the output file
        for value in values:
            # Make a copy of the original row
            new_row = row.copy()
            # Replace the value in the specified column with the current value
            new_row[column_to_split] = value.strip()
            # Write the new row to the output file
            writer.writerow(new_row)