def validate_schema(df, expected_columns):

    if set(df.columns) != set(expected_columns):
        raise ValueError("Schema mismatch")

    return True