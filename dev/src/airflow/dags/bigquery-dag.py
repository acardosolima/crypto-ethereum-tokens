import pandas as pd
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook


default_args = {
    'owner': 'Adriano',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'Crypto_Ethereum.Token',
    default_args=default_args,
    description='Gather sample data from bigquery-public-data.crypto_ethereum.tokens',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
)

def query_tokens_table(**kwargs):
    execution_date = kwargs['execution_date']
    file_path = f"/tmp/query_results_{execution_date.strftime('%Y%m%d%H%M')}.csv"
    
    hook = BigQueryHook(gcp_conn_id='bigquery_credentials', use_legacy_sql=True)
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM [bigquery-public-data.crypto_ethereum.tokens] LIMIT 10")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    df.to_csv(file_path, index=False)
    
    return file_path

start_task = PythonOperator(
    task_id='query_data',
    python_callable=query_tokens_table,
    dag=dag,
)

start_task 