import pandas as pd
from utils.schema_validator import validate_schema

def test_schema_validation():

    df = pd.DataFrame({
        "id":[1],
        "amount":[100],
        "currency":["USD"],
        "updated_at":["2024-01-01"]
    })

    expected = ["id","amount","currency","updated_at"]

    assert validate_schema(df, expected)