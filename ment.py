def generate_duplicates_dataframe(duplicates):
    data = {
        "Environment": [],
        "File Name": [],
        "Data Similarity": []
    }

    unique_names = set()  # Track unique names

    for duplicate in duplicates:
        if duplicate.name in unique_names:
            data["Environment"].append(duplicate.environment)
            data["File Name"].append(duplicate.new_path)
            data["Data Similarity"].append("Duplicate")
        else:
            unique_names.add(duplicate.name)

    df_duplicates = pd.DataFrame(data)
    return df_duplicates
