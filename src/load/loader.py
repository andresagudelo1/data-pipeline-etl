from sqlalchemy import text
import pandas as pd

def load_chunk(df, engine):

    df = df.drop_duplicates(subset=["id"])

    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT id FROM transactions"))
            existing_ids = {row[0] for row in result}
    except Exception:
        # la tabla no existe todavía
        existing_ids = set()

    df = df[~df["id"].isin(existing_ids)]

    if not df.empty:
        df.to_sql(
            "transactions",
            engine,
            if_exists="append",
            index=False,
            method="multi"
        )