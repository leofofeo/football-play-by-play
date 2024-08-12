import csv

def count_rows_in_csv(csv_file_path):
    with open(csv_file_path, 'r') as infile:
        reader = csv.reader(infile)
        row_count = sum(1 for row in reader)
    return row_count

# Usage
csv_file_path = 'data/play_by_play_1999.csv'
row_count = count_rows_in_csv(csv_file_path)
print("Total number of rows:", row_count)
