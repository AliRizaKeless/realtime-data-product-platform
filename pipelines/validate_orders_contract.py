import json
from pathlib import Path

import pandas as pd


contract_path = Path("contracts/orders_contract.json")
data_path = Path("data/silver/orders_cleaned.parquet")

with open(contract_path, "r", encoding="utf-8") as file:
    contract = json.load(file)

df = pd.read_parquet(data_path)

errors = []

for column in contract["columns"]:
    column_name = column["name"]

    if column["required"] and column_name not in df.columns:
        errors.append(f"Missing required column: {column_name}")

    if column_name in df.columns and column.get("unique", False):
        if df[column_name].duplicated().any():
            errors.append(f"Column must be unique: {column_name}")

if errors:
    print("Contract validation failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("Orders contract validation passed")