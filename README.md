# Retail Business Intelligence & Customer Decision Analytics

## Final version

This project is an upgraded version of the uploaded retail-sales analysis. The original work used Python/Pandas, Matplotlib and Excel; the final version adds SQL/MySQL, customer intelligence, statistics, market-basket analysis, forecasting, anomaly detection and a Power BI-ready reporting layer.

## Source validation

The canonical source is the **`data` sheet of the uploaded Excel workbook**. It contains:

- 9,800 rows
- 18 source columns
- 4,922 unique orders
- 793 customers
- 1,861 products
- 17 sub-categories
- 0 duplicate rows
- 11 missing postal codes

## Run the complete project

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/run_all.py
```

This validates the source, creates all analytical tables and creates the portfolio charts.

## MySQL

```bash
python src/load_to_mysql.py
```

Then execute:

1. `sql/schema.sql`
2. `sql/build_star_schema.sql`
3. `sql/analysis_queries.sql`

The Python loader is intentionally used instead of the Workbench CSV wizard. It validates that the loaded row count equals the 9,800 source rows.

## Where each project layer lives

| Layer | Location |
|---|---|
| Data | `data/raw/retail_sales.csv` |
| Python | `src/analysis_pipeline.py` |
| SQL | `sql/` |
| Business analysis | `outputs/tables/` + `outputs/charts/` |
| Statistics | `outputs/tables/statistical_tests.csv` |
| Customer intelligence | `customer_rfm.csv`, `customer_concentration.csv`, `cohort_retention.csv` |
| Forecasting | `forecast_model_comparison.csv`, `forecast_2019.csv` |
| Dashboard | `powerbi/DAX_Measures.md` |
| Recommendations | `docs/PROJECT_REPORT.md` |
| Interview prep | `docs/INTERVIEW_GUIDE.md` |
| Final report | `outputs/Retail_Business_Intelligence_Final_Report.pdf` |
| Final Excel report | `outputs/Retail_Business_Intelligence_Final_Report.xlsx` |

## Final analytical results

- Historical sales: **$2,261,536.78**
- Orders: **4,922**
- Customers: **793**
- Products: **1,861**
- Average order value: **$459.48**
- Average shipping time: **3.96 days**
- Median shipping time: **4 days**
- 2018 sales: **$722,052.02**
- Best holdout forecast model: **ETS Additive Damped**
- Best holdout MAPE: **18.10%**

## Important limitation

The source has no profit, cost, quantity, discount, inventory or returns fields. Do not claim profitability, margin, inventory optimization, discount effectiveness, CAC or true CLV from this dataset.

## Resume version

**Retail Business Intelligence & Customer Decision Analytics | Python, SQL, MySQL, Power BI**

- Analyzed 9,800 retail transactions across four years using Python/Pandas and SQL, developing reusable KPI, customer, product, regional and operational analytics.
- Built RFM segmentation, cohort retention and customer concentration analysis across 793 customers; found approximately 28.9% of customers accounted for 60% of historical sales.
- Implemented non-parametric statistical testing, sub-category market-basket analysis, anomaly detection and time-series forecasting with a 12-month holdout evaluation.
- Designed a MySQL star schema and Power BI decision dashboard covering executive KPIs, customer intelligence, product performance, operations and forecasting.
