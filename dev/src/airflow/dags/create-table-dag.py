from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime

default_args = {
    "owner": "Data Engineer",
    "retries": 0
}

dag = DAG(
    'Create-Table-dag',
    description='Create table to insert tokens data',
    schedule_interval=None,
    start_date= datetime(2024, 8, 5),
    catchup=False,
    default_args=default_args,
    max_active_runs=1,
    max_active_tasks=1
)

def create_table_postgres(**kwargs):
    
    pg_hook = PostgresHook(postgres_conn_id='postgres_credentials')
    pg_conn = pg_hook.get_conn()
    cursor = pg_conn.cursor()

    create_table_sql = """
        CREATE TABLE IF NOT EXISTS tokens (
            address TEXT,
            symbol TEXT,
            name TEXT,
            decimals INTEGER DEFAULT 0,
            total_supply TEXT,
            block_timestamp TEXT,
            block_number TEXT,
            block_hash TEXT,
            CONSTRAINT unique_address_block_hash UNIQUE (address, block_timestamp, block_hash)
        );
    """

    cursor.execute(create_table_sql)

    pg_conn.commit()
    cursor.close()
    pg_conn.close()

fetch_task = PythonOperator(
    task_id='query_bigquery_task',
    python_callable=create_table_postgres,
    dag=dag,
)