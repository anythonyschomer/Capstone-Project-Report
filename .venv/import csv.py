import csv

filename = 'C:\\Users\\14029\\Desktop\\Capstone Project\\Capstone-Project-Report\\top10s.csv'

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    row_count = sum(1 for row in csvreader)

print(f"The file {filename} contains {row_count} rows.")