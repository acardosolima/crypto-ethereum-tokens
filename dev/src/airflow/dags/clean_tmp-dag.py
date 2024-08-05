from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


dag = DAG(
    'Clean-Temp-folder',
    description='Clean temp folder used to persist data retrieved from BigQuery',
    schedule_interval=timedelta(weeks=1),
    start_date=datetime(2024, 8, 5),
    catchup=False,
    retries= 1,
    retry_delay= timedelta(minutes=5)
)

clean_temp_folder = BashOperator(
    task_id='clean_temp_task',
    bash_command='rm -rf /tmp/query_*',
    dag=dag,
)