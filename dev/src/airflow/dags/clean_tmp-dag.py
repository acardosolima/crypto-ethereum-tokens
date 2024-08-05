from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Data Engineer',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Clean-Temp-folder',
    default_args=default_args,
    description='Clean temp folder used to persist data retrieved from BigQuery',
    schedule_interval=timedelta(weeks=1),
    start_date=datetime(2024, 8, 5),
    catchup=False 
)

clean_temp_folder = BashOperator(
    task_id='clean_temp_task',
    bash_command='rm -r /tmp/query_*.json',
    dag=dag,
)