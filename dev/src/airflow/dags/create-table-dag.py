from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime

default_args = {
    'owner': 'Data Engineer',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 1),
    'retries': 0
}

dag = DAG(
    'Create-Table-dag',
    description='Create table to insert tokens data',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    max_active_runs=1,
    max_active_tasks=1
)

def create_table_postgres(**kwargs):
    
    pg_hook = PostgresHook(postgres_conn_id='postgres_credentials')
    pg_conn = pg_hook.get_conn()
    cursor = pg_conn.cursor()

    create_table_sql = """
        CREATE TABLE tokens (
            address TEXT NOT NULL,
            symbol TEXT,
            name TEXT,
            decimals INTEGER,
            total_supply BIGINT,
            block_timestamp TIMESTAMP NOT NULL,
            block_number BIGINT,
            block_hash TEXT NOT NULL,
            CONSTRAINT unique_address_block_hash UNIQUE (address, block_hash)
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