def test_extract_json(self):
        cov = coverage.Coverage()
        cov.start()
        
        mock_data = """[
            {color: "red",value: "#f00"},
            {color: "green",value: "#0f0},
            {color: "blue",value: "#00f"}]"""
        
        with patch("builtins.open", mock_open(read_data=mock_data)):
         -> keys = extract_json(mock_data)
            expected_keys = ["red", "green", "blue"]
        
            self.assertEqual(keys, expected_keys)
        
        cov.stop()
        cov.report()


# Finding the key for each test case and returning it 
def extract_json(json_list):
    first_level_key = []
    # going through each JSON object in JSon list
    for json_object in json_list:
        # getting each JSON Key  
     -> keys = list(json_object.keys()) 
        if keys:
            # only getting the first key -- which is the name, and putting it in the list  
            first_level_key.append(keys[0])
    return (first_level_key)
