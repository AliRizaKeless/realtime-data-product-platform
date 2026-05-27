import pandas as pd
from pathlib import Path

input_path = Path("data/bronze/orders.parquet")

df = pd.read_parquet(input_path)

# Basic cleaning
df["product"] = df["product"].str.upper()

# Remove duplicates
df = df.drop_duplicates()

# Filter invalid prices
df = df[df["price"] > 0]

output_path = Path("data/silver/orders_cleaned.parquet")
output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_parquet(output_path, index=False)

print("Silver layer created successfully")