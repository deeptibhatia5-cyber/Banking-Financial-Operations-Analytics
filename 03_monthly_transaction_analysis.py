import pandas as pd
df=pd.read_csv(r"C:\Users\HP\Downloads\banking_financial_operations_analytics_github_starter (1)\banking_financial_operations_analytics\data\raw\banking_transactions_10000.csv")
print(df.head(10))
print(df.tail(10))
print(df.shape)
print(df.describe)
print(df.columns.tolist())
print(df.dtypes)
df["Transaction_Date"]=pd.to_datetime(df["Transaction_Date"])
print(df.dtypes)
#missing value
print(df.isnull().sum())
#duplicated records
print(df.duplicated().sum())
print(df["Transaction_ID"].duplicated().sum())
Status_Count=(df["Transaction_Status"].value_counts())
print(Status_Count)
total_transaction=len(df)
Success_ratio=(
    Status_Count.get("Success",0)/total_transaction)*100
Failed_ratio=(
    Status_Count.get("Failed",0)/total_transaction)*100
Pending_ratio=(
    Status_Count.get("Pending",0)/total_transaction)*100
print(Success_ratio)
print(Failed_ratio)
print(Pending_ratio)
print(df["Payment_Method"].value_counts())
failed_transaction=df[df["Transaction_Status"]=="Failed"]
failure_by_method=failed_transaction["Payment_Method"].value_counts()
print(failure_by_method)
failure_by_method=failed_transaction["Region"].value_counts()
print(failure_by_method)
failure_analysis=df.groupby("Payment_Method").agg(
    Total_Transactions=("Transaction_ID","count"),
    Failed_Transactions=("Transaction_Status",
                         lambda x: (x == "Failed").sum())
)
failure_analysis["Failure_Rate"] = (
    failure_analysis["Failed_Transactions"] /
    failure_analysis["Total_Transactions"] * 100
)
failure_analysis["Failure_Rate"] = failure_analysis["Failure_Rate"].round(2)
print("\nFailure analysis by payment method")
print(failure_analysis.sort_values(
    by="Failure_Rate",ascending=False))
failure_analysis=df.groupby("Region").agg(
    Total_Transactions=("Transaction_ID","count"),
    Failed_Transactions=("Transaction_Status",
                         lambda x: (x == "Failed").sum())
)
failure_analysis["Failure_Rate"] = (
    failure_analysis["Failed_Transactions"] /
    failure_analysis["Total_Transactions"] * 100
)
failure_analysis["Failure_Rate"] = failure_analysis["Failure_Rate"].round(2)
print("\nFailure analysis by Region")
print(failure_analysis.sort_values(
    by="Failure_Rate",ascending=False))
failure_analysis["Failure_Rate"] = failure_analysis["Failure_Rate"].round(2)
print("\nFailure analysis by payment method")
print(failure_analysis.sort_values(
    by="Failure_Rate",ascending=False))
failure_analysis=df.groupby("Branch").agg(
    Total_Transactions=("Transaction_ID","count"),
    Failed_Transactions=("Transaction_Status",
                         lambda x: (x == "Failed").sum())
)
failure_analysis["Failure_Rate"] = (
    failure_analysis["Failed_Transactions"] /
    failure_analysis["Total_Transactions"] * 100
)
failure_analysis["Failure_Rate"] = failure_analysis["Failure_Rate"].round(2)
print("\nFailure analysis by Branch")
print(failure_analysis.sort_values(
    by="Failure_Rate",ascending=False))
# failure by payment method= Net banking
# region= North
# Branch= jaipur
net_banking_jaipur=df[
    (df["Payment_Method"]== "Net Banking") & (df["Branch"]=="Jaipur")]
print("Net Banking analysis in jaipur")
total_transaction=len(net_banking_jaipur)
print("\n Transaction Status")
print(net_banking_jaipur["Transaction_Status"].value_counts())
failed_transactions=(
    net_banking_jaipur["Transaction_Status"]=="Failed").sum()
Failed_ratio=(failed_transactions/total_transaction)*100
print(round(Failed_ratio,2))
# Compare all payment methods in Jaipur
jaipur_analysis=df[df["Branch"]=="Jaipur"]
jaipur_payment_analysis=jaipur_analysis.groupby("Payment_Method").agg(
    Total_Transactions=("Transaction_ID","count"),
    Failed_Transactions=("Transaction_Status",
                         lambda x: (x == "Failed").sum())
)
jaipur_payment_analysis["Failure_Rate"] = (
    jaipur_payment_analysis["Failed_Transactions"] /
    jaipur_payment_analysis["Total_Transactions"] * 100
)
jaipur_payment_analysis["Failure_Rate"] = jaipur_payment_analysis["Failure_Rate"].round(2)
print("\njaipur payment  analysis by payment method")
print(jaipur_payment_analysis.sort_values(
    by="Failure_Rate",ascending=False))
net_banking=df[df["Payment_Method"]=="Net Banking"]
net_banking_analysis=net_banking.groupby("Branch").agg(
    Total_Transactions=("Transaction_ID","count"),
    Failed_Transactions=("Transaction_Status",
                         lambda x: (x == "Failed").sum())
)
net_banking_analysis["Failure_Rate"] = (
    net_banking_analysis["Failed_Transactions"] /
  net_banking_analysis["Total_Transactions"] * 100
)
net_banking_analysis["Failure_Rate"] = net_banking_analysis["Failure_Rate"].round(2)
print("\n net_banking_analysis by payment method")
print(net_banking_analysis.sort_values(
    by="Failure_Rate",ascending=False))
df["Month"] = df["Transaction_Date"].dt.to_period("M")
print(df["Month"].value_counts().sort_index())
df.groupby("Month")
monthly_status=df.groupby(["Month","Transaction_Status"]).size()
print(monthly_status)
april_analysis=df[df["Month"]=="2025-04"]
april_payment_analysis=april_analysis.groupby("Payment_Method").agg(
    Total_Transactions=("Transaction_ID","count"),
    Failed_Transactions=("Transaction_Status",lambda x :(x=="Failed").sum())
    )
april_payment_analysis["Failed_Transactions"] = (
    april_payment_analysis["Failed_Transactions"].astype(int)
)
april_payment_analysis["Failure_Rate"]=(
    april_payment_analysis["Failed_Transactions"]/
    april_payment_analysis["Total_Transactions"]*100
    )
april_payment_analysis["Failure_Rate"]=april_payment_analysis["Failure_Rate"].round(2)
print("\n april_payment_analysis by payment method")
print(april_payment_analysis.sort_values( 
    by="Failure_Rate",ascending=False))
print(april_payment_analysis.dtypes)
monthly_failed = df.groupby("Month").agg(
    Total_Transactions=("Transaction_ID", "count"),
    Failed_Transactions=(
        "Transaction_Status",
        lambda x: (x == "Failed").sum()
    )
)

monthly_failed["Failure_Rate"] = (
    monthly_failed["Failed_Transactions"] /
    monthly_failed["Total_Transactions"] * 100
).round(2)

print(monthly_failed.sort_values(
    by="Month",
    ascending=False
))

monthly_status = df.groupby(
    ["Month", "Transaction_Status"]
).size().unstack(fill_value=0)

print(monthly_status)
print(monthly_status.columns)



































































































































