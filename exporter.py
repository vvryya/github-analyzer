import csv
import os

def save_as_csv(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    if not data:
        print("Nothing to save.")
        return
    
    keys = data[0].keys()
    with open(output_path, mode = 'w', newline = '', encoding = 'utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        for row in data:
            row_copy = row.copy()
            if isinstance(row_copy.get("languages"), dict):
                row_copy["languages"] = ", ".join(row_copy["languages"].keys())
            writer.writerow(row_copy)