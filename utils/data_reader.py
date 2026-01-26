import json
import csv
from pathlib import Path

# Function for reading JSON data file
def read_json(file_path):
    p = Path(file_path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

# Function for reading CSV data file
def read_csv_1(file_path):
    p = Path(file_path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with p.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [(row["username"], row["password"], row["expected"]) for row in reader]

def read_csv(file_path):
    p = Path(file_path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with p.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

# # čita CSV fajl i vraća listu tuple-ova za pytest parametrizaciju
# def read_csv_data(file_path):
#     with open(file_path, newline='', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         data = []
#         for row in reader:
#             data.append((row['username'], row['password'], row['expected']))
#         return data
