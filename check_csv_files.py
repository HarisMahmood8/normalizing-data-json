import csv
from collections import Counter

def check_duplicate_paths(csv_file):
    file_paths = []

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            file_paths.append(row[0])

    duplicates = [path for path, count in Counter(file_paths).items() if count > 1]

    if duplicates:
        print("Duplicate paths found:")
        for path in duplicates:
            print(path)
    else:
        print("No duplicates found.")


csv_file = 'file_paths.csv'
check_duplicate_paths(csv_file)
