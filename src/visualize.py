from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
T=ROOT/"outputs/tables"; C=ROOT/"outputs/charts"; C.mkdir(exist_ok=True)
def save(name): plt.tight_layout(); plt.savefig(C/name,dpi=180,bbox_inches="tight"); plt.close()
def main():
    monthly=pd.read_csv(T/"monthly_sales.csv",parse_dates=["Month Start"])
    yearly=pd.read_csv(T/"yearly_sales.csv")
    region=pd.read_csv(T/"region_sales.csv")
    category=pd.read_csv(T/"category_sales.csv")
    products=pd.read_csv(T/"top_products.csv").head(10)
    customers=pd.read_csv(T/"top_customers.csv").head(10)
    rfm=pd.read_csv(T/"customer_rfm.csv")
    plt.figure(); plt.plot(monthly["Month Start"],monthly.Sales,marker="o"); plt.title("Monthly Historical Sales Trend"); plt.ylabel("Historical Sales ($)"); save("01_monthly_sales_trend.png")
    plt.figure(); plt.bar(yearly.Year.astype(str),yearly.Sales); plt.title("Annual Historical Sales"); plt.ylabel("Historical Sales ($)"); save("02_annual_sales.png")
    x=region.sort_values("Sales"); plt.figure(); plt.barh(x.Region,x.Sales); plt.title("Historical Sales by Region"); plt.xlabel("Historical Sales ($)"); save("03_sales_by_region.png")
    x=category.sort_values("Sales"); plt.figure(); plt.barh(x.Category,x.Sales); plt.title("Historical Sales by Category"); plt.xlabel("Historical Sales ($)"); save("04_sales_by_category.png")
    x=products.sort_values("Sales"); plt.figure(figsize=(11,6)); plt.barh(x["Product Name"],x.Sales); plt.title("Top 10 Products by Historical Sales"); plt.xlabel("Historical Sales ($)"); save("05_top_10_products.png")
    x=customers.sort_values("Sales"); plt.figure(figsize=(10,6)); plt.barh(x["Customer Name"],x.Sales); plt.title("Top 10 Customers by Historical Sales"); plt.xlabel("Historical Sales ($)"); save("06_top_10_customers.png")
    x=rfm.groupby("Segment").Monetary.sum().sort_values(); plt.figure(figsize=(9,5)); bars=plt.barh(x.index,x.values); plt.title("Historical Sales by RFM Segment"); plt.xlabel("Historical Sales ($)")
    for b,v in zip(bars,x.values): plt.text(v,b.get_y()+b.get_height()/2,f"${v:,.0f}",va="center")
    save("07_rfm_historical_sales.png")
    comp=pd.read_csv(T/"forecast_model_comparison.csv").sort_values("MAPE %"); plt.figure(figsize=(9,5)); plt.barh(comp.Model,comp["MAPE %"]); plt.title("Forecast Model Comparison"); plt.xlabel("Holdout MAPE (%)"); save("08_forecast_model_comparison.png")
    back=pd.read_csv(T/"forecast_2019.csv"); hist=pd.read_csv(T/"monthly_sales.csv"); hist["Month Start"]=pd.to_datetime(hist["Month Start"]); back["Forecast Month"]=pd.to_datetime(back["Forecast Month"])
    plt.figure(figsize=(11,5)); plt.plot(hist["Month Start"],hist.Sales,label="Historical"); plt.plot(back["Forecast Month"],back["Forecast Sales"],marker="o",label="2019 Forecast"); plt.title("Historical Sales and 2019 Forecast"); plt.ylabel("Sales ($)"); plt.legend(); save("09_2019_forecast.png")
if __name__=="__main__": main()
