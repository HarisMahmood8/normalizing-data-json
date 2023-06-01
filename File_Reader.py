import json

def test_file_generator(data):
    with open(data, 'r') as f:
        data = json.load(f)

    if isinstance(data, list):
        for index, item in enumerate(data):
            file_name = f"test_case_{index}.txt"
            with open(file_name, 'w') as f:
                f.write(json.dumps(item)) 
    else:
        print("🚨🚨🚨🚨🚨🚨🚨🚨no array🚨🚨🚨🚨🚨🚨🚨🚨")


input_data = 'testing_data.json'
test_file_generator(input_data)
