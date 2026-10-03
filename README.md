# Retail Business Intelligence & Customer Decision Analytics

A business-focused retail analytics project using **Python, SQL/MySQL, statistical analysis, customer analytics, market-basket analysis, forecasting, anomaly detection, and Power BI-ready reporting**.

The objective is to transform raw retail transaction data into actionable insights around **sales performance, customers, products, shipping operations, and future sales planning**.

---

## Project Overview

This project analyzes **9,800 retail transactions** covering four years of sales activity.

The analysis combines:

- Python & Pandas for data cleaning and analysis
- SQL/MySQL for structured business analytics
- RFM analysis for customer segmentation
- Cohort and retention analysis
- Customer concentration analysis
- Product and Pareto analysis
- Market-basket analysis
- Shipping and operational analysis
- Statistical hypothesis testing
- Anomaly detection
- Time-series forecasting
- Power BI-ready KPI and DAX measures

---

## Dataset

| Metric | Value |
|---|---:|
| Transactions | 9,800 |
| Unique Orders | 4,922 |
| Customers | 793 |
| Products | 1,861 |
| Sub-categories | 17 |
| Duplicate Rows | 0 |
| Missing Postal Codes | 11 |
| Historical Sales | $2,261,536.78 |

The primary dataset is available at:

`data/raw/retail_sales.csv`

---

## Key Business Insights

### Sales Performance

- Historical sales totaled **$2.26M**.
- 2018 generated **$722,052.02**, the highest annual sales in the dataset.
- Average order value was approximately **$459.48**.

### Customer Intelligence

RFM analysis segmented customers into five customer groups:

- Champions: 122
- Loyal / High Value: 255
- Needs Attention: 262
- At Risk: 87
- New / Promising: 67

Approximately **28.9% of customers generated 60% of historical sales**, highlighting customer concentration.

### Product Intelligence

Product analysis includes:

- Category and sub-category performance
- Top products
- Pareto analysis
- Market-basket associations

The strongest observed sub-category association by lift was **Fasteners + Machines**, with a lift of approximately **1.66**.

This represents an association for potential cross-selling analysis, not a causal relationship.

### Shipping Operations

Average shipping duration was approximately **3.96 days**, with a median of **4 days**.

Shipping performance was analyzed across:

- Shipping modes
- Regions
- Customer segments
- Product categories
- Time periods

### Statistical Analysis

Non-parametric statistical tests were used where appropriate.

Key findings included:

- A statistically significant difference in shipping duration between Standard Class and First Class.
- A statistically significant difference in shipping duration across regions.
- No statistically significant difference in order value across customer segments in the tested data.

### Forecasting

Multiple forecasting approaches were compared using a fixed **12-month holdout period**.

The best-performing model on the fixed holdout period was:
**ETS Additive Damped**

Holdout MAPE:

**18.10%**

The forecast should be treated as a planning baseline rather than a guaranteed future outcome.

### Anomaly Detection

An IQR-based analysis identified **November 2018** as an unusually high-sales month, which can be investigated further using business context.

---

## Project Architecture

```text
Raw Retail Data
      │
      ▼
Data Validation & Cleaning
      │
      ├──────────────► Python / Pandas
      │
      ├──────────────► SQL / MySQL
      │
      ├──────────────► Customer Analytics
      │                  ├── RFM
      │                  ├── Cohort Retention
      │                  └── Customer Concentration
      │
      ├──────────────► Product Analytics
      │                  ├── Pareto Analysis
      │                  └── Market Basket Analysis
      │
      ├──────────────► Statistical Analysis
      │
      ├──────────────► Forecasting
      │
      └──────────────► Anomaly Detection
                         │
                         ▼
                 Power BI Reporting Layer
                         │
                         ▼
                Business Recommendations
