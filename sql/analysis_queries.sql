USE retail_analytics;

-- Total historical sales
SELECT ROUND(SUM(sales),2) AS historical_sales FROM fact_sales;

-- Monthly sales + month-over-month growth
WITH m AS (
 SELECT DATE_FORMAT(order_date,'%Y-%m') year_month,SUM(sales) sales
 FROM fact_sales GROUP BY DATE_FORMAT(order_date,'%Y-%m')
)
SELECT year_month,ROUND(sales,2) sales,
 ROUND((sales-LAG(sales) OVER(ORDER BY year_month))/
       NULLIF(LAG(sales) OVER(ORDER BY year_month),0)*100,2) mom_growth_pct
FROM m ORDER BY year_month;

-- Top products
SELECT p.product_name,p.category,p.sub_category,ROUND(SUM(f.sales),2) historical_sales
FROM fact_sales f JOIN dim_product p ON p.product_key=f.product_key
GROUP BY p.product_key,p.product_name,p.category,p.sub_category
ORDER BY historical_sales DESC LIMIT 10;

-- Regional ranking
WITH r AS (
 SELECT g.region,SUM(f.sales) sales
 FROM fact_sales f JOIN dim_geography g ON g.geography_key=f.geography_key
 GROUP BY g.region
)
SELECT region,ROUND(sales,2) historical_sales,
DENSE_RANK() OVER(ORDER BY sales DESC) sales_rank
FROM r ORDER BY sales_rank;

-- Customer concentration
WITH c AS (
 SELECT customer_key,SUM(sales) historical_sales
 FROM fact_sales GROUP BY customer_key
)
SELECT dc.customer_id,dc.customer_name,ROUND(c.historical_sales,2) historical_sales,
ROUND(100*SUM(c.historical_sales) OVER(ORDER BY c.historical_sales DESC)/
      SUM(c.historical_sales) OVER(),2) cumulative_sales_pct
FROM c JOIN dim_customer dc ON dc.customer_key=c.customer_key
ORDER BY historical_sales DESC;

-- Shipping performance
SELECT ship_mode,COUNT(*) line_items,ROUND(AVG(shipping_days),2) avg_shipping_days,
ROUND(AVG(sales),2) avg_line_sales
FROM fact_sales GROUP BY ship_mode ORDER BY avg_shipping_days;
