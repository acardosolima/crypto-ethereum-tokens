from pandas import DataFrame
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook


dag = DAG(
    'Bigquery-Postgres-dag',
    owner= 'Data Engineer',
    description='Ingest data from bigquery-public-data.crypto_ethereum.tokens to PostgreSQL',
    schedule_interval='@daily',
    depends_on_past= False,
    start_date= datetime(2024, 8, 4),
    catchup=True,
    retries= 2,
    retry_delay= timedelta(minutes=5)
)

def query_tokens_table(**kwargs):    
    execution_date = kwargs['data_interval_start'] 
    beg_date = execution_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = beg_date.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)

    print(beg_date)
    print(end_date)
    
    file_path = f"/tmp/query_results_{execution_date.strftime('%Y%m%d%H%M')}.csv"

    hook = BigQueryHook(gcp_conn_id='bigquery_credentials', use_legacy_sql=True)
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM [bigquery-public-data.crypto_ethereum.tokens] WHERE block_timestamp >= '{beg_date}' and block_timestamp < '{end_date}';")
    rows = cursor.fetchall()
    
    df = DataFrame(rows)
    df.to_csv(file_path, index=False, header=False)

    return file_path

def save_to_postgres(**kwargs):
    ti = kwargs['ti']
    file_path = ti.xcom_pull(task_ids='query_bigquery_task')
    
    pg_hook = PostgresHook(postgres_conn_id='postgres_credentials')
    pg_conn = pg_hook.get_conn()
    cursor = pg_conn.cursor()

    copy_sql = f"""
    COPY tokens(address, symbol, name, decimals,total_supply,block_timestamp,block_number,block_hash)
    FROM STDIN WITH (FORMAT CSV, DELIMITER ',');
    """
    
    with open(file_path, 'r') as f:            
        cursor.copy_expert(sql=copy_sql, file=f)
    
    pg_conn.commit()
    cursor.close()
    pg_conn.close()


fetch_task = PythonOperator(
    task_id='query_bigquery_task',
    python_callable=query_tokens_table,
    dag=dag,
)

save_task = PythonOperator(
    task_id='save_to_postgres_task',
    python_callable=save_to_postgres,
    provide_context=True,
    dag=dag,
)

fetch_task >> save_task