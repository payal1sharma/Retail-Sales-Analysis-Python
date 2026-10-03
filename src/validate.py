import pandas as pd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/raw/retail_sales.csv')
assert df.shape==(9800,18)
assert df.duplicated().sum()==0
print('PASS — 9,800 rows × 18 columns')
print('PASS — 0 duplicate rows')
print(f'PASS — {df["Order ID"].nunique():,} orders')
print(f'PASS — {df["Customer ID"].nunique():,} customers')
print(f'PASS — ${df["Sales"].sum():,.2f} historical sales')
