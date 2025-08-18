# PythonDataExercise

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Este repositorio contiene cinco proyectos avanzados de ingeniería y migración de datos en Python, diseñados para demostrar habilidades profesionales en ETL, orquestación, análisis, integración de APIs y automatización de reportes con SQL y Python.

## Estructura de Carpetas

- [`etl_sql/`](./etl_sql): Pipeline ETL robusto para migración y transformación de datos entre fuentes SQL y archivos. Incluye validación, logging profesional, configuración flexible y pruebas.
- [`data_pipeline_orchestration/`](./data_pipeline_orchestration): Orquestación avanzada de pipelines de datos con Airflow y Python. Incluye DAGs reales, manejo de dependencias, logging y configuración YAML.
- [`advanced_data_analysis/`](./advanced_data_analysis): Análisis avanzado de datos con pandas, SQL y visualización. Incluye notebooks, scripts, configuración YAML y pruebas.
- [`api_to_sql_integration/`](./api_to_sql_integration): Integración robusta de datos desde APIs REST a SQL con validación, logging y configuración YAML.
- [`sql_reporting_automation/`](./sql_reporting_automation): Automatización profesional de reportes y dashboards SQL con Python. Incluye generación de reportes, visualización, logging y configuración YAML.

## Navegación y Ejecución

Cada carpeta contiene su propio `README.md` con instrucciones detalladas de instalación, configuración y ejecución. Para comenzar con cualquier ejercicio:

1. Navega a la carpeta del proyecto deseado:
   ```bash
   cd <nombre_del_proyecto>
   ```
   Por ejemplo:
   ```bash
   cd etl_sql
   ```
2. Instala las dependencias:
   ```bash
   uv pip install -r requirements.txt
   ```
3. Consulta el `README.md` de cada proyecto para instrucciones específicas de ejecución y pruebas.

## Ejemplo de Estructura de Proyecto

```
PythonDataExercise/
├── etl_sql/
├── data_pipeline_orchestration/
├── advanced_data_analysis/
├── api_to_sql_integration/
├── sql_reporting_automation/
└── README.md
```

## Requisitos Generales
- Python 3.9+
- [uv](https://github.com/astral-sh/uv) para la gestión de dependencias (puedes usar pip si lo prefieres)

## Propósito

Estos ejercicios están pensados para practicar y demostrar maestría en ingeniería de datos, migración, automatización y análisis profesional en Python y SQL.

## Recursos Útiles
- [Documentación oficial de Python](https://docs.python.org/3/)
- [Documentación de pandas](https://pandas.pydata.org/docs/)
- [Documentación de SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentación de Airflow](https://airflow.apache.org/docs/)
- [Documentación de uv](https://github.com/astral-sh/uv)

---

Para dudas o sugerencias, abre un issue o contacta al autor del repositorio.
