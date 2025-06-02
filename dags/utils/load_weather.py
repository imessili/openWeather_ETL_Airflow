from airflow.hooks.postgres_hook import PostgresHook
import os

def load_weather_data_to_postgres(**context):

    file_path = context['ti'].xcom_pull(task_ids='extract-weather-hourly')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found at path: {file_path}")

    # copy_expert command = very fast bulk data loading
    copy_sql = """
        COPY open_weather.open_weather_api_tbl (
            id, city_name, main, date_time, description, main_temp,
            main_feels_like, main_temp_min, main_temp_max, main_pressure,
            main_humidity, main_sea_level, main_grnd_level, wind_speed,
            wind_deg, wind_gust, clouds_all, icon, base, visibility, dt,
            timezone, cod, coord_lon, coord_lat, sys_country, sys_sunrise,
            sys_sunset, sys_type, sys_id
        )
        FROM STDIN WITH CSV HEADER DELIMITER AS ','
    """

    hook = PostgresHook(postgres_conn_id='my_postgres_conn')

    # Load the file using copy_expert
    with open(file_path, 'r') as f:
        hook.copy_expert(sql=copy_sql, filename=file_path)

    print(f"Successfully loaded data using COPY from {file_path}")