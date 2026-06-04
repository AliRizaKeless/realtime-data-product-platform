import pandas as pd
from pathlib import Path

input_path = Path("data/gold/product_sales_summary.parquet")
output_path = Path("dashboards/product_sales_summary.csv")

df = pd.read_parquet(input_path)

output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("Gold layer exported to dashboard CSV successfully")