# data_pipeline_orchestration

Orquestación avanzada de pipelines de datos con Airflow y Python. Incluye DAGs reales, manejo de dependencias, logging y configuración YAML.

## Estructura
- `src/`: DAGs, utilidades y configuración
- `logs/`: Logs de ejecución
- `tests/`: Pruebas unitarias

## Instalación
```bash
uv pip install -r requirements.txt
```

## Ejecución
Configura Airflow y coloca los DAGs en la carpeta `src/`. Personaliza `src/config.yaml`.

## Características
- DAGs complejos con dependencias y retries
- Integración con SQL y APIs
- Logging profesional
- Configuración flexible
- Pruebas unitarias
