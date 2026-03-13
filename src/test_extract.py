from db.connection import get_source_engine
from extract.extractor import extract_incremental

engine = get_source_engine()

df = extract_incremental(engine, "2024-01-02")

print(df)