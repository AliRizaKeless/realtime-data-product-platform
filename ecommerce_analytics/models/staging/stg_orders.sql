select
    order_id,
    customer_name,
    product,
    price,
    country,
    created_at
from read_parquet('../data/silver/orders_cleaned.parquet')