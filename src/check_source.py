from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///source.db")

df = pd.read_sql("SELECT * FROM transactions", engine)

print(df)