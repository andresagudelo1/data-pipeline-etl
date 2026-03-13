from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///source.db")

data = {
    "id": [1,2,3,4],
    "amount": [100,200,300,400],
    "currency": ["USD","USD","EUR","COP"],
    "updated_at": [
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
        "2024-01-04"
    ]
}

df = pd.DataFrame(data)

df.to_sql("transactions", engine, if_exists="replace", index=False)

print("Base de datos creada con datos de prueba")