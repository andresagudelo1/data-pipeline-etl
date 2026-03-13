import pandas as pd

def extract_incremental(engine, last_timestamp):

    query = f"""
    SELECT *
    FROM transactions
    WHERE updated_at > '{last_timestamp}'
    """

    df = pd.read_sql(query, engine)

    return df