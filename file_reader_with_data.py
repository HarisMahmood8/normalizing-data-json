import json
import csv
import os

def test_file_generator(data):
    file_paths = []

    with open(data, 'r') as f:
        data = json.load(f)

    if isinstance(data, list):
        for index, item in enumerate(data):
            file_name = f"test_case_{index}.json"
            file_path = os.path.join(os.getcwd(), file_name)
            with open(file_path, 'w') as f:
                f.write(json.dumps(item)) 
            file_paths.append(file_path)

    else:
        print("🚨❌🚨❌🚨❌no array❌🚨❌🚨❌🚨")

    save_paths_to_csv(file_paths)


def save_paths_to_csv(file_paths):
    csv_file = 'file_paths.csv'
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['File Path'])
        for path in file_paths:
            writer.writerow([path])

    print(f"Saved to {csv_file}")


input_data = 'testing_data.json'
test_file_generator(input_data)
