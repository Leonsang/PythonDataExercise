# etl_sql

Pipeline ETL robusto para migración y transformación de datos entre fuentes SQL y archivos. Incluye validación, logging profesional, configuración flexible y pruebas.

## Estructura
- `src/`: Código fuente y configuración
- `data/`: Datos de entrada/salida y logs
- `tests/`: Pruebas unitarias

## Instalación
```bash
uv pip install -r requirements.txt
```

## Ejecución
```bash
python src/etl_pipeline.py --config src/config.yaml
```

## Características
- Extracción desde CSV, SQL, o APIs
- Transformaciones complejas y validación de datos
- Carga eficiente a SQL
- Logging y manejo de errores avanzado
- Configuración por YAML
- Pruebas unitarias

## Uso
Personaliza `src/config.yaml` para tus fuentes y destino. El pipeline es modular y fácil de extender.
