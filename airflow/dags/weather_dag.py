from airflow import DAG
# CHANGED: Airflow 3 moves these to the 'standard' provider
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime
import sys
import os

# Add the dags folder to the path so we can import the script
sys.path.append(os.path.dirname(__file__))
from fetch_weather import fetch_and_load_weather

# Define the DAG
with DAG(
    dag_id='weather_elt_pipeline',
    start_date=datetime(2023, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    # Task 1: Run the Python Ingestion Script
    task_extract_load = PythonOperator(
        task_id='extract_and_load',
        python_callable=fetch_and_load_weather
    )

# Task 2: Run dbt to transform the data
    # We add --log-path and --target-path to write files to a temporary folder 
    # instead of the read-only DAGs folder.
    dbt_cmd = (
        "dbt run "
        "--project-dir /usr/local/airflow/dags/weather_transform "
        "--profiles-dir /usr/local/airflow/dags/weather_transform "
        "--log-path /tmp "
        "--target-path /tmp/target"
    )
    
    task_transform = BashOperator(
        task_id='transform_data',
        bash_command=dbt_cmd
    )

    # Set dependency
    task_extract_load >> task_transform