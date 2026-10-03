# Architecture

```text
9,800-row CSV
    │
    ▼
Python / Pandas
cleaning + feature engineering
    │
    ├──────────────► Statistics / RFM / Cohorts / Basket / Forecast
    │
    ▼
MySQL raw_sales
    │
    ▼
Star schema
dim_customer ─┐
dim_product ──┤
dim_geography ├── fact_sales
dim_date ─────┘
    │
    ▼
SQL analytics
    │
    ▼
Power BI
Executive | Customer | Product | Operations & Forecast
    │
    ▼
Business recommendations
```

**Fact grain:** one source transaction row (`Row ID`).
