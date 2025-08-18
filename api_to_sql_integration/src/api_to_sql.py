import argparse
import requests
import pandas as pd
import yaml
from sqlalchemy import create_engine
from loguru import logger
import sys
from pathlib import Path
import time

logger.remove()
logger.add(sys.stderr, level="INFO")

def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def extract_api(api_cfg):
    for attempt in range(api_cfg.get('retries', 3)):
        try:
            logger.info(f"Extrayendo datos de API: {api_cfg['url']}")
            resp = requests.get(api_cfg['url'], timeout=api_cfg.get('timeout', 10))
            resp.raise_for_status()
            return pd.DataFrame(resp.json())
        except Exception as e:
            logger.warning(f"Intento {attempt+1} fallido: {e}")
            time.sleep(2)
    raise RuntimeError('No se pudo extraer datos de la API')

def validate_data(df):
    logger.info("Validando datos...")
    if df.isnull().sum().sum() > 0:
        logger.warning("Datos nulos detectados. Se eliminarán filas incompletas.")
        df = df.dropna()
    return df

def transform(df):
    logger.info("Transformando datos...")
    # Ejemplo: normalización de columnas string
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip().str.title()
    return df

def load_sql(df, db_uri, table):
    logger.info(f"Cargando datos a SQL: {db_uri}, tabla: {table}")
    engine = create_engine(db_uri)
    df.to_sql(table, engine, if_exists='replace', index=False)
    logger.info("Carga completada.")

def main(config_path):
    config = load_config(config_path)
    df = extract_api(config['api'])
    df = validate_data(df)
    df = transform(df)
    load_sql(df, config['destination']['db_uri'], config['destination']['table'])
    logger.info('Integración API-SQL finalizada.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Integración API a SQL')
    parser.add_argument('--config', type=str, default='src/config.yaml', help='Ruta del archivo de configuración')
    args = parser.parse_args()
    main(args.config)
