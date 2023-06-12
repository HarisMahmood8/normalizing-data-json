import unittest
import os
import json
from create_files_from_json import create_files_from_json_folder


class TestJsonFileHandling(unittest.TestCase):
    def create_temp_environment(self):
        self.test_folder = 'test_data'
        os.makedirs(self.test_folder, exist_ok=True)

    def delete_temp_environment(self):
        os.system(f"rm -rf {self.test_folder}")

    def create_json_file(self, file_path, data):
        with open(file_path, 'w') as f:
            json.dump(data, f)

    def testing_create_json_file(self):
        json_data1 = [
            {
                "name": "John",
                "age": 30,
                "city": "New York"
            },
            {
                "name": "Jane",
                "age": 25,
                "city": "Los Angeles"
            }
        ]
        json_data2 = [
            {
                "name": "Mark",
                "age": 35,
                "city": "Chicago"
            }
        ]
        self.create_json_file(f"{self.test_folder}/file1.json", json_data1)
        self.create_json_file(f"{self.test_folder}/subfolder1/file2.json", json_data2)

        create_files_from_json_folder(self.test_folder)

        self.assertTrue(os.path.exists(f"{self.test_folder}/file1.json_0.txt"))
        self.assertTrue(os.path.exists(f"{self.test_folder}/file1.json_1.txt"))
        self.assertTrue(os.path.exists(f"{self.test_folder}/subfolder1/file2.json_0.txt"))

        with open(f"{self.test_folder}/file1.json_0.txt", 'r') as f:
            file1_0_data = json.load(f)
            self.assertEqual(file1_0_data, json_data1[0])
        with open(f"{self.test_folder}/file1.json_1.txt", 'r') as f:
            file1_1_data = json.load(f)
            self.assertEqual(file1_1_data, json_data1[1])
        with open(f"{self.test_folder}/subfolder1/file2.json_0.txt", 'r') as f:
            file2_0_data = json.load(f)
            self.assertEqual(file2_0_data, json_data2[0])


if __name__ == '__main__':
    unittest.main()
