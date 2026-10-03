USE retail_analytics;

INSERT INTO dim_customer(customer_id,customer_name,segment)
SELECT DISTINCT `Customer ID`,`Customer Name`,Segment FROM raw_sales;

INSERT INTO dim_product(product_id,product_name,category,sub_category)
SELECT DISTINCT `Product ID`,`Product Name`,Category,`Sub-Category` FROM raw_sales;

INSERT INTO dim_geography(country,city,state,postal_code,region)
SELECT DISTINCT Country,City,State,`Postal Code`,Region FROM raw_sales;

INSERT INTO dim_date(date_key,full_date,year,quarter,month,month_name,year_month)
SELECT DISTINCT
 CAST(DATE_FORMAT(`Order Date`,'%Y%m%d') AS UNSIGNED),
 DATE(`Order Date`),YEAR(`Order Date`),QUARTER(`Order Date`),MONTH(`Order Date`),
 MONTHNAME(`Order Date`),DATE_FORMAT(`Order Date`,'%Y-%m')
FROM raw_sales WHERE `Order Date` IS NOT NULL;

INSERT INTO fact_sales
(row_id,order_id,order_date,ship_date,ship_mode,customer_key,product_key,geography_key,sales,shipping_days)
SELECT
 r.`Row ID`,r.`Order ID`,DATE(r.`Order Date`),DATE(r.`Ship Date`),r.`Ship Mode`,
 c.customer_key,p.product_key,g.geography_key,r.Sales,
 DATEDIFF(DATE(r.`Ship Date`),DATE(r.`Order Date`))
FROM raw_sales r
JOIN dim_customer c ON c.customer_id=r.`Customer ID`
JOIN dim_product p ON p.product_id=r.`Product ID`
JOIN dim_geography g
 ON g.country=r.Country AND g.city=r.City AND g.state=r.State
 AND (g.postal_code <=> r.`Postal Code`) AND g.region=r.Region;
