from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='test_postgres_connection',
    default_args=default_args,
    schedule_interval=None,
    tags=['test'],
    description='Test connection to Postgres from Airflow',
) as dag:

    test_postgres_conn = PostgresOperator(
        task_id='test_connection',
        postgres_conn_id='my_postgres_conn',  # Replace with your connection ID
        sql='SELECT 1;',
    )