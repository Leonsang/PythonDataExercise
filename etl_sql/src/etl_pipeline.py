import argparse
import pandas as pd
import yaml
from sqlalchemy import create_engine, text
from loguru import logger
import sys
from pathlib import Path

logger.remove()
logger.add(sys.stderr, level="INFO")

def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def extract_csv(path):
    logger.info(f"Extrayendo datos desde CSV: {path}")
    return pd.read_csv(path)

def extract_sql(uri, query):
    logger.info(f"Extrayendo datos desde SQL: {uri}")
    engine = create_engine(uri)
    return pd.read_sql(query, engine)

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
        df[col] = df[col].str.strip().str.upper()
    return df

def load_sql(df, uri, table):
    logger.info(f"Cargando datos a SQL: {uri}, tabla: {table}")
    engine = create_engine(uri)
    df.to_sql(table, engine, if_exists='replace', index=False)
    logger.info("Carga completada.")

def main(config_path):
    config = load_config(config_path)
    src = config['source']
    dst = config['destination']
    if src['type'] == 'csv':
        df = extract_csv(src['path'])
    elif src['type'] == 'sql':
        df = extract_sql(src['uri'], src['query'])
    else:
        raise ValueError('Tipo de fuente no soportado')
    df = validate_data(df)
    df = transform(df)
    load_sql(df, dst['uri'], dst['table'])
    logger.info('Pipeline ETL finalizado.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ETL Pipeline')
    parser.add_argument('--config', type=str, default='src/config.yaml', help='Ruta del archivo de configuración')
    args = parser.parse_args()
    main(args.config)
