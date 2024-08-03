from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

def check_postgres_connection():
    print("Testing PostgreSQL connection...")

default_args = {
    'owner': 'Adriano',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': days_ago(1),
    'retries': 0
}

with DAG(
    'test_postgres_connection',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    test_query = """
    SELECT now();
    """

    test_postgres_task = PostgresOperator(
        task_id='test_postgres_connection_task',
        postgres_conn_id='PostgresK8',
        sql=test_query,
    )

    test_postgres_task
