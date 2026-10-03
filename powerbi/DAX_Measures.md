# Power BI Build Specification

## Model relationships

```text
dim_customer 1 ─── * fact_sales * ─── 1 dim_product
                         |
                         ├──────────── 1 dim_geography
                         └──────────── 1 dim_date
```

## Measures

```DAX
Historical Sales = SUM(fact_sales[sales])

Orders = DISTINCTCOUNT(fact_sales[order_id])

Customers = DISTINCTCOUNT(dim_customer[customer_id])

Products = DISTINCTCOUNT(dim_product[product_id])

Average Order Value = DIVIDE([Historical Sales], [Orders])

Average Shipping Days = AVERAGE(fact_sales[shipping_days])

Historical Sales LY =
CALCULATE([Historical Sales], SAMEPERIODLASTYEAR(dim_date[full_date]))

YoY Growth % =
DIVIDE([Historical Sales]-[Historical Sales LY],[Historical Sales LY])
```

## Page 1 — Executive Overview
Cards: Historical Sales, Orders, Customers, AOV, YoY Growth, Avg Shipping Days.
Charts: monthly trend, category, region, segment.

## Page 2 — Customer Intelligence
RFM segment sales, customer concentration/Pareto, top customers, cohort retention.

## Page 3 — Product Intelligence
Category/sub-category sales, top products, product Pareto, market-basket table.

## Page 4 — Operations & Forecast
Shipping duration by mode/region, forecast vs historical, forecast model comparison, anomaly table.

Use **Historical Sales**, not Revenue or Profit, in titles unless a source field explicitly represents revenue.
