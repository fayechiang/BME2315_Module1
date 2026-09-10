import csv

file_path = "/Users/fayechiang/Library/Mobile Documents/com~apple~CloudDocs/Computational BME/Module 1/Metadata and Protein Data for Module 1.csv"

with open(file_path, mode="r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)
    column_headers = next(reader)

print(*column_headers, sep="\n")