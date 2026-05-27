from faker import Faker
import pandas as pd
import random
from pathlib import Path
from datetime import datetime

fake = Faker()

orders = []

for i in range(100):
    orders.append({
        "order_id": i + 1,
        "customer_name": fake.name(),
        "product": random.choice([
            "Laptop",
            "Phone",
            "Keyboard",
            "Monitor"
        ]),
        "price": random.randint(100, 3000),
        "country": fake.country(),
        "created_at": datetime.utcnow()
    })

df = pd.DataFrame(orders)

output_path = Path("data/bronze/orders.parquet")
output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_parquet(output_path, index=False)

print("Bronze orders parquet created successfully")