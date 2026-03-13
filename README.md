# Data Pipeline ETL

Pipeline backend desarrollado en Python para extraer datos desde un sistema legado y cargarlos en PostgreSQL para análisis en Power BI.

## Arquitectura

Source DB → Python ETL → PostgreSQL → Power BI

## Características

- Extracción incremental basada en timestamp
- Procesamiento por lotes (chunking)
- Concurrency con ThreadPoolExecutor
- Retry pattern con exponential backoff
- Validación de esquema
- Docker containerization
- Tests automatizados
- CI/CD con Azure Pipelines

## Ejecutar proyecto

```bash
docker-compose up -d
python src/pipeline.py