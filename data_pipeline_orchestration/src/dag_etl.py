import os
import yaml
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from loguru import logger
import pandas as pd
from sqlalchemy import create_engine

def load_config():
    with open(os.path.join(os.path.dirname(__file__), 'config.yaml'), 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def extract(**context):
    config = load_config()
    src = config['source']
    logger.info(f"Extrayendo datos desde {src['type']}")
    if src['type'] == 'csv':
        df = pd.read_csv(src['path'])
    elif src['type'] == 'sql':
        engine = create_engine(src['uri'])
        df = pd.read_sql(src['query'], engine)
    else:
        raise ValueError('Tipo de fuente no soportado')
    context['ti'].xcom_push(key='data', value=df.to_json())

def transform(**context):
    import json
    df = pd.read_json(context['ti'].xcom_pull(key='data'))
    logger.info("Transformando datos...")
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip().str.upper()
    context['ti'].xcom_push(key='data', value=df.to_json())

def load(**context):
    import json
    config = load_config()
    dst = config['destination']
    df = pd.read_json(context['ti'].xcom_pull(key='data'))
    engine = create_engine(dst['uri'])
    df.to_sql(dst['table'], engine, if_exists='replace', index=False)
    logger.info("Datos cargados en SQL.")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_pipeline_dag',
    default_args=default_args,
    description='DAG ETL profesional',
    schedule_interval='@daily',
    catchup=False
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    provide_context=True,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    provide_context=True,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    provide_context=True,
    dag=dag
)

extract_task >> transform_task >> load_task
