"""Reproducible end-to-end retail analytics pipeline."""
from pathlib import Path
from collections import Counter
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.tsa.holtwinters import ExponentialSmoothing

ROOT=Path(__file__).resolve().parents[1]
RAW_DATA=ROOT/"data/raw/retail_sales.csv"
OUT=ROOT/"outputs/tables"

def save(df,name): df.to_csv(OUT/name,index=False)

def main():
    df=pd.read_csv(RAW_DATA)
    expected=['Row ID','Order ID','Order Date','Ship Date','Ship Mode','Customer ID','Customer Name','Segment',
               'Country','City','State','Postal Code','Region','Product ID','Category','Sub-Category','Product Name','Sales']
    assert df.shape==(9800,18), f"Expected 9800x18, got {df.shape}"
    assert list(df.columns)==expected
    assert df.duplicated().sum()==0

    df["Order Date"]=pd.to_datetime(df["Order Date"],format="mixed",dayfirst=True,errors="raise")
    df["Ship Date"]=pd.to_datetime(df["Ship Date"],format="mixed",dayfirst=True,errors="raise")
    df["Shipping Days"]=(df["Ship Date"]-df["Order Date"]).dt.days
    df["Year"]=df["Order Date"].dt.year
    df["Month"]=df["Order Date"].dt.month
    df["Month Start"]=df["Order Date"].dt.to_period("M").dt.to_timestamp()
    df["Quarter"]=df["Order Date"].dt.quarter
    df["Year-Month"]=df["Order Date"].dt.strftime("%Y-%m")

    quality=pd.DataFrame({
      "Check":["Rows","Columns","Duplicate rows","Missing postal codes","Invalid order dates","Invalid ship dates","Negative sales","Zero sales","Negative shipping days"],
      "Result":[len(df),len(df.columns),df.duplicated().sum(),df["Postal Code"].isna().sum(),df["Order Date"].isna().sum(),df["Ship Date"].isna().sum(),(df["Sales"]<0).sum(),(df["Sales"]==0).sum(),(df["Shipping Days"]<0).sum()]
    })
    save(quality,"data_quality.csv")

    orders=df.groupby("Order ID").agg(Order_Date=("Order Date","min"),Customer_ID=("Customer ID","first"),Customer_Name=("Customer Name","first"),Segment=("Segment","first"),Region=("Region","first"),Sales=("Sales","sum"),Product_Count=("Product ID","nunique")).reset_index()
    save(orders,"orders.csv")
    save(pd.DataFrame({"Metric":["Historical Sales","Orders","Customers","Products","Sub-Categories","Average Order Value","Average Shipping Days","Median Shipping Days"],
                       "Value":[df.Sales.sum(),df["Order ID"].nunique(),df["Customer ID"].nunique(),df["Product ID"].nunique(),df["Sub-Category"].nunique(),df.Sales.sum()/df["Order ID"].nunique(),df["Shipping Days"].mean(),df["Shipping Days"].median()]}),"kpis.csv")
    save(df.groupby("Year",as_index=False)["Sales"].sum(),"yearly_sales.csv")
    save(df.groupby("Month Start",as_index=False)["Sales"].sum(),"monthly_sales.csv")
    save(df.groupby("Category",as_index=False)["Sales"].sum().sort_values("Sales",ascending=False),"category_sales.csv")
    save(df.groupby("Sub-Category",as_index=False)["Sales"].sum().sort_values("Sales",ascending=False),"subcategory_sales.csv")
    save(df.groupby("Region",as_index=False)["Sales"].sum().sort_values("Sales",ascending=False),"region_sales.csv")
    save(df.groupby("Segment",as_index=False)["Sales"].sum().sort_values("Sales",ascending=False),"segment_sales.csv")
    save(df.groupby(["Product ID","Product Name","Category","Sub-Category"],as_index=False)["Sales"].sum().sort_values("Sales",ascending=False).head(25),"top_products.csv")
    save(df.groupby(["Customer ID","Customer Name"],as_index=False)["Sales"].sum().sort_values("Sales",ascending=False).head(25),"top_customers.csv")

    as_of=df["Order Date"].max()+pd.Timedelta(days=1)
    rfm=df.groupby("Customer ID").agg(Customer_Name=("Customer Name","first"),Recency=("Order Date",lambda x:(as_of-x.max()).days),Frequency=("Order ID","nunique"),Monetary=("Sales","sum"),First_Purchase=("Order Date","min"),Last_Purchase=("Order Date","max")).reset_index()
    rfm["R"]=pd.qcut(rfm.Recency,5,labels=[5,4,3,2,1],duplicates="drop").astype(int)
    rfm["F"]=pd.qcut(rfm.Frequency.rank(method="first"),5,labels=[1,2,3,4,5]).astype(int)
    rfm["M"]=pd.qcut(rfm.Monetary.rank(method="first"),5,labels=[1,2,3,4,5]).astype(int)
    rfm["RFM Score"]=rfm[["R","F","M"]].sum(axis=1)
    rfm["Segment"]=np.select([rfm["RFM Score"]>=13,rfm["RFM Score"]>=10,(rfm.R>=4)&(rfm.F<=2),(rfm.R<=2)&(rfm.F>=3)],["Champions","Loyal/High Value","New/Promising","At Risk"],default="Needs Attention")
    save(rfm,"customer_rfm.csv")

    conc=rfm[["Customer ID","Customer_Name","Monetary","Frequency"]].sort_values("Monetary",ascending=False).rename(columns={"Monetary":"Historical Sales","Frequency":"Orders"})
    conc["Cumulative Historical Sales %"]=conc["Historical Sales"].cumsum()/conc["Historical Sales"].sum()*100
    conc["Cumulative Customers %"]=np.arange(1,len(conc)+1)/len(conc)*100
    save(conc,"customer_concentration.csv")

    first=df.groupby("Customer ID")["Order Date"].min().dt.to_period("M")
    cx=df[["Customer ID","Order Date"]].copy()
    cx["Cohort Month"]=cx["Customer ID"].map(first)
    cx["Order Month"]=cx["Order Date"].dt.to_period("M")
    cx["Cohort Index"]=cx["Order Month"].astype(int)-cx["Cohort Month"].astype(int)+1
    cc=cx.groupby(["Cohort Month","Cohort Index"])["Customer ID"].nunique()
    cs=cc.xs(1,level=1)
    ret=cc.unstack().div(cs,axis=0).reset_index()
    ret.columns=[str(c) for c in ret.columns]
    ret["Cohort Month"]=ret["Cohort Month"].astype(str)
    save(ret,"cohort_retention.csv")

    oi=df.groupby("Order ID")["Sub-Category"].apply(lambda s:sorted(set(s)))
    ic,pc=Counter(),Counter()
    for items in oi:
        for a in items: ic[a]+=1
        for i in range(len(items)):
            for j in range(i+1,len(items)): pc[(items[i],items[j])]+=1
    rows=[]
    for (a,b),t in pc.items():
        if t<4: continue
        support=t/len(oi)
        rows.append([a,b,t,support,t/ic[a],t/ic[b],support/((ic[a]/len(oi))*(ic[b]/len(oi)))])
    basket=pd.DataFrame(rows,columns=["Sub-Category A","Sub-Category B","Orders Together","Support","Confidence A→B","Confidence B→A","Lift"]).sort_values(["Lift","Orders Together"],ascending=False).head(25)
    save(basket,"market_basket_subcategory.csv")

    std=df.loc[df["Ship Mode"]=="Standard Class","Shipping Days"]; fc=df.loc[df["Ship Mode"]=="First Class","Shipping Days"]
    mw=stats.mannwhitneyu(std,fc,alternative="two-sided")
    kwr=stats.kruskal(*[g["Shipping Days"].values for _,g in df.groupby("Region")])
    kwc=stats.kruskal(*[g["Sales"].values for _,g in orders.groupby("Segment")])
    save(pd.DataFrame([
      ["Mann–Whitney U","Shipping duration: Standard Class vs First Class",mw.statistic,mw.pvalue],
      ["Kruskal–Wallis","Shipping duration across regions",kwr.statistic,kwr.pvalue],
      ["Kruskal–Wallis","Order value across customer segments",kwc.statistic,kwc.pvalue]
    ],columns=["Test","Question","Statistic","p_value"]),"statistical_tests.csv")

    monthly=df.groupby("Month Start")["Sales"].sum().sort_index()
    train=monthly.iloc[:-12]; test=monthly.iloc[-12:]
    candidates=[]
    naive=pd.Series(train.iloc[-12:].values,index=test.index)
    candidates.append(("Seasonal Naive",naive))
    specs=[("ETS Additive Damped","add","add",True),("ETS Additive","add","add",False),("ETS Additive Seasonal, No Trend",None,"add",False),("ETS Multiplicative","mul","mul",False)]
    for name,trend,seasonal,damped in specs:
        model=ExponentialSmoothing(train,trend=trend,damped_trend=damped if trend else False,seasonal=seasonal,seasonal_periods=12,initialization_method="estimated").fit()
        candidates.append((name,model.forecast(12)))
    def met(p): return {"MAE":np.mean(np.abs(test-p)),"RMSE":np.sqrt(np.mean((test-p)**2)),"MAPE %":np.mean(np.abs((test-p)/test))*100}
    fm=pd.DataFrame([{"Model":name,**met(pred)} for name,pred in candidates]).sort_values("MAPE %")
    save(fm,"forecast_model_comparison.csv")
    best=fm.iloc[0]["Model"]
    pred=dict(candidates)[best]
    if best=="Seasonal Naive":
        future=pd.Series([monthly.iloc[-12+i] for i in range(12)],index=pd.date_range(monthly.index[-1]+pd.offsets.MonthBegin(),periods=12,freq="MS"))
    else:
        trend="add"; seasonal="add"; damped=(best=="ETS Additive Damped")
        if best=="ETS Additive Seasonal, No Trend": trend=None; damped=False
        if best=="ETS Multiplicative": trend="mul"; seasonal="mul"; damped=False
        model=ExponentialSmoothing(monthly,trend=trend,damped_trend=damped if trend else False,seasonal=seasonal,seasonal_periods=12,initialization_method="estimated").fit()
        future=model.forecast(12)
    save(pd.DataFrame({"Forecast Month":future.index.strftime("%Y-%m"),"Forecast Sales":future.values}),"forecast_2019.csv")

    q1,q3=monthly.quantile(.25),monthly.quantile(.75); iqr=q3-q1
    ma=monthly.reset_index(); ma.columns=["Month Start","Sales"]; ma["Lower Bound"]=q1-1.5*iqr; ma["Upper Bound"]=q3+1.5*iqr; ma["Anomaly"]=(ma.Sales<ma["Lower Bound"])|(ma.Sales>ma["Upper Bound"])
    save(ma,"monthly_anomalies.csv")
    oq1,oq3=orders.Sales.quantile(.25),orders.Sales.quantile(.75); oi=oq3-oq1
    oa=orders.copy(); oa["Lower Bound"]=oq1-1.5*oi; oa["Upper Bound"]=oq3+1.5*oi; oa["Anomaly"]=(oa.Sales<oa["Lower Bound"])|(oa.Sales>oa["Upper Bound"])
    save(oa[oa.Anomaly].sort_values("Sales",ascending=False).head(50),"order_anomalies.csv")

    df.to_csv(ROOT/"data/processed/retail_sales_enriched.csv",index=False)
    print("Pipeline complete.")
if __name__=="__main__": main()
