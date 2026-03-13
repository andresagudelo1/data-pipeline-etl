from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///target.db")

df = pd.read_sql("SELECT * FROM transactions", engine)

print(df)