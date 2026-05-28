import pandas as pd
from pathlib import Path

input_path = Path("data/silver/orders_cleaned.parquet")

df = pd.read_parquet(input_path)

gold_df = (
    df.groupby("product")
    .agg(
        total_orders=("order_id", "count"),
        total_revenue=("price", "sum"),
        average_price=("price", "mean")
    )
    .reset_index()
)

output_path = Path("data/gold/product_sales_summary.parquet")
output_path.parent.mkdir(parents=True, exist_ok=True)

gold_df.to_parquet(output_path, index=False)

print("Gold layer created successfully")