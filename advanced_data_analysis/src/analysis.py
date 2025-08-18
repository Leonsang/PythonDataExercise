import argparse
import pandas as pd
import yaml
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from loguru import logger
import sys
from pathlib import Path

logger.remove()
logger.add(sys.stderr, level="INFO")

def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def main(config_path):
    config = load_config(config_path)
    db_uri = config['input']['db_uri']
    table = config['input']['table']
    engine = create_engine(db_uri)
    df = pd.read_sql_table(table, engine)
    logger.info(f"Datos cargados: {df.shape}")
    logger.info(f"Columnas: {df.columns.tolist()}")
    # Estadísticas descriptivas
    print(df.describe(include='all'))
    # Visualización avanzada
    if 'monto' in df.columns:
        plt.figure(figsize=(10,6))
        sns.histplot(df['monto'], kde=True)
        plt.title('Distribución de montos')
        plt.savefig(Path(config['output']['report_dir']) / 'hist_monto.png')
    if 'categoria' in df.columns and 'monto' in df.columns:
        plt.figure(figsize=(10,6))
        sns.boxplot(x='categoria', y='monto', data=df)
        plt.title('Boxplot por categoría')
        plt.savefig(Path(config['output']['report_dir']) / 'boxplot_categoria.png')
    logger.info('Análisis avanzado finalizado.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Análisis avanzado de datos')
    parser.add_argument('--config', type=str, default='src/config.yaml', help='Ruta del archivo de configuración')
    args = parser.parse_args()
    main(args.config)
