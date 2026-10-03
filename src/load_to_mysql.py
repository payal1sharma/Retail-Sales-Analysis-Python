from getpass import getpass
from pathlib import Path
from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine,text
ROOT=Path(__file__).resolve().parents[1]
csv=ROOT/"data/raw/retail_sales.csv"
user=input("MySQL user [root]: ").strip() or "root"
password=getpass("MySQL password: ")
engine=create_engine(f"mysql+mysqlconnector://{user}:{quote_plus(password)}@localhost:3306/retail_analytics")
df=pd.read_csv(csv)
df["Order Date"]=pd.to_datetime(df["Order Date"],format="mixed",dayfirst=True)
df["Ship Date"]=pd.to_datetime(df["Ship Date"],format="mixed",dayfirst=True)
df.to_sql("raw_sales",engine,if_exists="replace",index=False,chunksize=1000,method="multi")
with engine.connect() as conn: count=conn.execute(text("SELECT COUNT(*) FROM raw_sales")).scalar()
assert count==len(df),f"Expected {len(df)}, loaded {count}"
print(f"PASS — {count:,} rows loaded into retail_analytics.raw_sales")
