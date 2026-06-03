from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator


PROJECT_ROOT = "/opt/airflow/project"


with DAG(
    dag_id="data_product_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["data-platform", "medallion", "data-quality"],
) as dag:

    start = EmptyOperator(task_id="start")

    generate_orders = BashOperator(
        task_id="generate_orders_bronze",
        bash_command=f"cd {PROJECT_ROOT} && python pipelines/generate_orders.py",
    )

    transform_orders = BashOperator(
        task_id="transform_orders_silver",
        bash_command=f"cd {PROJECT_ROOT} && python pipelines/transform_orders.py",
    )

    create_gold = BashOperator(
        task_id="create_gold_sales_metrics",
        bash_command=f"cd {PROJECT_ROOT} && python pipelines/create_gold_layer.py",
    )

    validate_contract = BashOperator(
        task_id="validate_orders_contract",
        bash_command=f"cd {PROJECT_ROOT} && python pipelines/validate_orders_contract.py",
    )

    end = EmptyOperator(task_id="end")

    start >> generate_orders >> transform_orders >> create_gold >> validate_contract >> end