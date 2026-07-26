import pandas as pd

# Read dataset
df = pd.read_csv("data.csv")

# First five rows
print(df.head())

# Dataset size
print(df.shape)

# Column names
print(df.columns)

# Dataset information
print("\n===== DATASET INFORMATION =====")
df.info()

# Statistical summary
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# Missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Duplicate rows
print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

# Data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

# Create a copy
df_clean = df.copy()

# Check missing values
print("\nMissing Values:")
print(df_clean.isnull().sum())

# Check duplicates
print("\nDuplicates Before:", df_clean.duplicated().sum())

# Remove duplicates
df_clean.drop_duplicates(inplace=True)

print("Duplicates After:", df_clean.duplicated().sum())

# Convert Order Date to datetime
df_clean["Order Date"] = pd.to_datetime(df_clean["Order Date"], dayfirst=True)

# Check data types
print("\nData Types:")
print(df_clean.dtypes)

print("\n===== BASIC ANALYSIS =====")

# Total Sales
total_sales = df_clean["Sales"].sum().round(2)
print("Total Sales:", total_sales)

# Average Sales
average_sales = df_clean["Sales"].mean().round(2)
print("Average Sales:", average_sales)

# Highest Sale
highest_sale = df_clean["Sales"].max()
print("Highest Sale:", highest_sale)

# Lowest Sale
lowest_sale = df_clean["Sales"].min()
print("Lowest Sale:", lowest_sale)

# Total Orders
total_orders = df_clean["Order ID"].nunique()
print("Total Orders:", total_orders)

# Average Order Value
average_order_value = total_sales / total_orders
print("Average Order Value:", round(average_order_value, 2))

print("\n===== SALES BY REGION =====")
print(df_clean.groupby("Region")["Sales"].sum())

print("\n===== SALES BY SEGMENT =====")
print(df_clean.groupby("Segment")["Sales"].sum())

df_clean["Month"] = df_clean["Order Date"].dt.month_name()

print("\n===== MONTHLY SALES =====")
print(df_clean.groupby("Month")["Sales"].sum())

print("\n===== TOP 10 PRODUCTS =====")
print(
    df_clean.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 CUSTOMERS =====")
print(
    df_clean.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 HIGHEST SALES =====")
print(df_clean.sort_values(by="Sales", ascending=False).head(10))

print("\n===== LOWEST SALES =====")
print(df_clean.sort_values(by="Sales").head(10))

print("\n===== SALES > 1000 =====")
print(df_clean[df_clean["Sales"] > 1000].head())

print("\n===== TECHNOLOGY CATEGORY =====")
print(df_clean[df_clean["Category"] == "Technology"].head())

print("\n===== WEST REGION =====")
print(df_clean[df_clean["Region"] == "West"].head())

print("\n===== WEST + TECHNOLOGY =====")
print(
    df_clean[
        (df_clean["Region"] == "West") &
        (df_clean["Category"] == "Technology")
    ].head()
)

print("\n===== CATEGORY COUNT =====")
print(df_clean["Category"].value_counts())

print("\n===== REGION COUNT =====")
print(df_clean["Region"].value_counts())

import matplotlib.pyplot as plt

print("\n===== Sales by Region (Bar Chart) =====")
sales_by_region = df_clean.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
sales_by_region.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()


print("\n===== Sales by Category =====")
sales_by_category = df_clean.groupby("Category")["Sales"].sum()

plt.figure(figsize=(7,7))
sales_by_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()


top_products = (
    df_clean.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 7))
top_products.plot(kind="barh")

plt.title("Top 10 Products")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.gca().invert_yaxis()      # Highest sales at the top
plt.tight_layout()


month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

df_clean["Month"] = df_clean["Order Date"].dt.strftime("%b")

monthly_sales = (
    df_clean.groupby("Month")["Sales"]
    .sum()
    .reindex(month_order)
)

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)
plt.tight_layout()

# Top 10 Customers by Sales
top_customers = (
    df_clean.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

top_customers.plot(kind="barh")

plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Customer Name")

# Highest sales at the top
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()