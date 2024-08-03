from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    'read_csv_and_copy_to_postgres',
    default_args=default_args,
    description='Read a CSV file and use COPY command to insert it into PostgreSQL',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
)

def copy_csv_to_postgres(**kwargs):
    file_path = '/tmp/data.csv'
    
    pg_hook = PostgresHook(postgres_conn_id='PostgresK8')
    pg_conn = pg_hook.get_conn()
    cursor = pg_conn.cursor()

    copy_sql = f"""
    COPY your_table (column1, column2)
    FROM STDIN WITH CSV HEADER
    DELIMITER AS ','
    """
    
    with open(file_path, 'r') as f:
        cursor.copy_expert(sql=copy_sql, file=f)
    
    pg_conn.commit()
    cursor.close()
    pg_conn.close()

copy_task = PythonOperator(
    task_id='copy_csv_to_postgres_task',
    python_callable=copy_csv_to_postgres,
    provide_context=True,
    dag=dag,
)

copy_task