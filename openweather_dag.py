from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from openweather_requests import openweather_etl

default_args = {
    "owner": "raul",
    "depends_on_past": False,
    "start_date": datetime(2024, 8, 22),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    "openweather_dag",
    default_args=default_args,
    description="DAG with ETL process",
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id="complete_openweather_etl",
    python_callable=openweather_etl,
    dag=dag,
)

run_etl
