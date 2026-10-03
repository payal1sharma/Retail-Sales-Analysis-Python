# Data Dictionary

| Field | Meaning | Main use |
|---|---|---|
| Row ID | Source row identifier | Data grain / audit |
| Order ID | Order identifier | Orders / basket analysis |
| Order Date | Order placement date | Time series / cohort |
| Ship Date | Shipping date | Shipping duration |
| Ship Mode | Shipping service | Operations |
| Customer ID | Customer identifier | Customer analytics |
| Customer Name | Customer label | Reporting |
| Segment | Business customer segment | Segment analysis |
| Country/City/State | Geography | Regional analysis |
| Postal Code | Postal code | Geography |
| Region | Sales region | Regional analysis |
| Product ID | Product identifier | Product analysis |
| Category/Sub-Category | Product hierarchy | Product/basket analysis |
| Product Name | Product label | Product reporting |
| Sales | Transaction sales value | Historical sales KPI |

Derived fields include Shipping Days, Year, Month, Quarter, RFM metrics, cohort index, basket support/confidence/lift, forecast values and anomaly flags.

**Not available:** profit, cost, quantity, discount, inventory, returns and customer acquisition cost. Do not infer these.
