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
