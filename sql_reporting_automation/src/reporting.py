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
    query = config['input']['query']
    report_dir = Path(config['output']['report_dir'])
    report_dir.mkdir(parents=True, exist_ok=True)
    engine = create_engine(db_uri)
    df = pd.read_sql(query, engine)
    logger.info(f"Datos cargados: {df.shape}")
    print(df)
    # Visualización avanzada
    plt.figure(figsize=(10,6))
    sns.barplot(x='categoria', y='total', data=df)
    plt.title('Ventas por Categoría')
    plt.ylabel('Total')
    plt.tight_layout()
    out_path = report_dir / 'ventas_categoria.png'
    plt.savefig(out_path)
    logger.info(f'Reporte guardado en {out_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automatización de reportes SQL')
    parser.add_argument('--config', type=str, default='src/config.yaml', help='Ruta del archivo de configuración')
    args = parser.parse_args()
    main(args.config)
