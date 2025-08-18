from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

def tarea_extract():
    logging.info('Extracción de datos')
    # Simulación de extracción

def tarea_transform():
    logging.info('Transformación de datos')
    # Simulación de transformación

def tarea_load():
    logging.info('Carga de datos en SQL')
    # Simulación de carga

default_args = {
    'start_date': datetime(2023, 1, 1),
}

dag = DAG(
    'simple_etl_dag',
    default_args=default_args,
    description='DAG de ejemplo para ETL',
    schedule_interval=None,
    catchup=False
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=tarea_extract,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=tarea_transform,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=tarea_load,
    dag=dag
)

extract_task >> transform_task >> load_task
