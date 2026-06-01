from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="data_product_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    start = EmptyOperator(task_id="start")

    bronze = EmptyOperator(task_id="bronze_layer")

    silver = EmptyOperator(task_id="silver_layer")

    gold = EmptyOperator(task_id="gold_layer")

    validation = EmptyOperator(task_id="contract_validation")

    end = EmptyOperator(task_id="end")

    start >> bronze >> silver >> gold >> validation >> end