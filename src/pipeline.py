from db.connection import get_source_engine, get_target_engine
from extract.extractor import extract_incremental
from utils.chunking import chunk_dataframe
from utils.schema_validator import validate_schema
from load.retry_loader import safe_load
from concurrent.futures import ThreadPoolExecutor

def run_pipeline():

    source = get_source_engine()
    target = get_target_engine()

    last_timestamp = "2024-01-01"

    data = extract_incremental(source, last_timestamp)

    print("Filas extraídas:", len(data))
    print(data.head())

    expected_columns = [
        "id",
        "amount",
        "currency",
        "updated_at"
    ]

    validate_schema(data, expected_columns)

    chunks = list(chunk_dataframe(data))

    print("Número de chunks:", len(chunks))

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(lambda chunk: safe_load(chunk, target), chunks)

    print("Pipeline terminado")


if __name__ == "__main__":
    run_pipeline()