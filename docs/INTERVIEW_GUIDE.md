# Interview Guide

## 60-second answer

"I started with a 9,800-row retail transaction dataset and upgraded a basic Pandas/Excel analysis into an end-to-end BI workflow. I used Python for data quality, feature engineering, RFM, cohort analysis, market-basket analysis, statistical testing, anomaly detection and forecasting. I used MySQL to create a star schema and demonstrate reusable SQL analytics, and designed a four-page Power BI reporting layer. One important analytical decision was to avoid profit or inventory claims because the source data does not contain cost, profit, quantity or inventory fields."

## Why RFM?
Recency measures how recently a customer bought, Frequency how often they bought, and Monetary historical sales value.

## Why not true CLV?
The dataset lacks margin, retention assumptions, future value and acquisition cost inputs needed for a defensible CLV estimate.

## Why non-parametric tests?
Retail transaction values and shipping durations can be skewed. Mann–Whitney and Kruskal–Wallis avoid requiring normality of the compared groups.

## Why a holdout forecast?
A forecast should be evaluated on observations not used to fit the model. Here the last 12 months are held out.

## Why market basket?
It converts order-level product/category co-occurrence into support, confidence and lift measures that can generate cross-sell hypotheses.

## Why star schema?
It separates reusable dimensions such as customer/product/geography/date from the transaction fact table and makes BI querying easier.

## Strong SQL topics
JOIN, GROUP BY, CASE, CTE, LAG, DENSE_RANK, window functions, cumulative totals, date functions and aggregation.

## Questions to prepare
1. What is the fact-table grain?
2. Why is sales not the same as profit?
3. How did you calculate AOV?
4. How did you construct RFM?
5. What does lift mean?
6. Why use Mann–Whitney instead of a t-test?
7. What does a p-value mean?
8. How did you avoid data leakage in forecasting?
9. Why did you use a 12-month holdout?
10. What would you request from the business next?
