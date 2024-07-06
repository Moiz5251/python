import glob
import csv

# Create a new empty CSV file for the output
with open('output.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Keep track of whether we've written the header row yet
    header_written = False

    # Loop through all CSV files in the current directory
    for filename in glob.glob('*.csv'):

        # Open the CSV file
        with open(filename, 'r', newline='') as infile:
            reader = csv.reader(infile)

            # Check if the file has any rows
            try:
                first_row = next(reader)
            except StopIteration:
                continue

            # Skip the first row (assuming it's a header row)
            try:
                next(reader)
            except StopIteration:
                pass

            # Write the header row if we haven't written it yet
            if not header_written:
                try:
                    header = next(reader)
                except StopIteration:
                    continue
                writer.writerow(header)
                header_written = True

            # Write only the first sheet's data rows to the output file
            for row in reader:
                if row and row[0].lower() == 'sheet 1':
                    break
                row = [cell.strip() for cell in row]
                writer.writerow(row)
