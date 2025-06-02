from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from utils.fetch_weather import fetch_weather_data
from utils.load_weather import load_weather_data_to_postgres


default_args = {
    'start_date': datetime(2025, 5, 30),
    'catchup': False,
}

with DAG(
    dag_id='open_weather_etl',
    default_args=default_args,
    schedule_interval='0 * * * *',
    tags=['weather'],
) as dag:

    extract_weather = PythonOperator(
        task_id='extract-weather-hourly',
        python_callable=fetch_weather_data,
    )

    load_to_postgres = PythonOperator(
    task_id='load-to-postgres-hourly',
    python_callable=load_weather_data_to_postgres,
    provide_context=True
    )

    extract_weather >> load_to_postgres


