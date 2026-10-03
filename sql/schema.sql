CREATE DATABASE IF NOT EXISTS retail_analytics;
USE retail_analytics;

DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS dim_product;
DROP TABLE IF EXISTS dim_customer;
DROP TABLE IF EXISTS dim_geography;

CREATE TABLE dim_customer (
 customer_key INT AUTO_INCREMENT PRIMARY KEY,
 customer_id VARCHAR(30) NOT NULL UNIQUE,
 customer_name VARCHAR(150),
 segment VARCHAR(50)
);

CREATE TABLE dim_product (
 product_key INT AUTO_INCREMENT PRIMARY KEY,
 product_id VARCHAR(40) NOT NULL UNIQUE,
 product_name VARCHAR(255),
 category VARCHAR(80),
 sub_category VARCHAR(80)
);

CREATE TABLE dim_geography (
 geography_key INT AUTO_INCREMENT PRIMARY KEY,
 country VARCHAR(100),
 city VARCHAR(100),
 state VARCHAR(100),
 postal_code INT NULL,
 region VARCHAR(50),
 UNIQUE(country,city,state,postal_code,region)
);

CREATE TABLE dim_date (
 date_key INT PRIMARY KEY,
 full_date DATE NOT NULL UNIQUE,
 year INT,
 quarter INT,
 month INT,
 month_name VARCHAR(20),
 year_month VARCHAR(7)
);

CREATE TABLE fact_sales (
 sales_key BIGINT AUTO_INCREMENT PRIMARY KEY,
 row_id INT,
 order_id VARCHAR(40),
 order_date DATE,
 ship_date DATE,
 ship_mode VARCHAR(50),
 customer_key INT,
 product_key INT,
 geography_key INT,
 sales DECIMAL(14,4),
 shipping_days INT,
 FOREIGN KEY(customer_key) REFERENCES dim_customer(customer_key),
 FOREIGN KEY(product_key) REFERENCES dim_product(product_key),
 FOREIGN KEY(geography_key) REFERENCES dim_geography(geography_key),
 INDEX(order_id), INDEX(order_date), INDEX(customer_key), INDEX(product_key)
);
