import pandas as pd
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook


default_args = {
    'owner': 'Data Engineer',
    'depends_on_past': False,
    'start_date': datetime(2024, 7, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'Ingest-tokens-dataset',
    description='Ingest data from bigquery-public-data.crypto_ethereum.tokens to PostgreSQL',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True,
)

def query_tokens_table(**kwargs):
    file_path = f"/tmp/query_results_{{ ds_nodash }}.csv"
    
    hook = BigQueryHook(gcp_conn_id='bigquery_credentials', use_legacy_sql=True)
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM [bigquery-public-data.crypto_ethereum.tokens] WHERE block_timestamp > "{{ ds_nodash }}-01 00:00:00"')
    rows = cursor.fetchall()
  
    df = pd.DataFrame(rows)
    df.to_csv(file_path, index=False)
    
    return file_path

fetch_task = PythonOperator(
    task_id='query_data',
    python_callable=query_tokens_table,
    dag=dag,
)

fetch_task 