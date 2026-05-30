import subprocess
import sys


steps = [
    "pipelines/generate_orders.py",
    "pipelines/transform_orders.py",
    "pipelines/create_gold_layer.py",
    "pipelines/validate_orders_contract.py",
]

for step in steps:
    print(f"Running {step}...")
    subprocess.run([sys.executable, step], check=True)

print("Full pipeline completed successfully")