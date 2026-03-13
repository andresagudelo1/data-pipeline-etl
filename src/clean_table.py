from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres")

with engine.begin() as conn:
    conn.execute(text("DELETE FROM transactions"))

print("Tabla transactions limpiada")