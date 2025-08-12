
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {"owner": "you", "retries": 0}

with DAG(
    dag_id="smart_retail_monitoring_and_retrain",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@weekly",
    catchup=False,
    default_args=default_args,
) as dag:

    make_data = BashOperator(task_id="make_data", bash_command="python -m src.data.make_mock_data")
    monitor = BashOperator(task_id="data_drift_report", bash_command="python -m src.monitoring.data_drift")
    train_xgb = BashOperator(task_id="train_xgb", bash_command="python -m src.models.train_xgb")
    train_uplift = BashOperator(task_id="train_uplift", bash_command="python -m src.uplift.train_uplift")

    make_data >> monitor >> [train_xgb, train_uplift]
