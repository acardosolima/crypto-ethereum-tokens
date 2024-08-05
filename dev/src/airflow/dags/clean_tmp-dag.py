from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "Data Engineer",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    'Clean-Temp-folder',
    description='Clean temp folder used to persist data retrieved from BigQuery',
    schedule_interval=timedelta(weeks=1),
    start_date=datetime(2024, 8, 5),
    catchup=False,
    default_args=default_args
)

clean_temp_folder = BashOperator(
    task_id='clean_temp_task',
    bash_command='rm -rf /tmp/query_*',
    dag=dag,
)