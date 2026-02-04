import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("C:/Users/JEAN JEASEN/Documents/DataAnalytics/plantation_analytics_project/data/raw/plantation_data.csv")

df["date"] = pd.to_datetime(df["date"])
df["profit"] = df["sales_revenue"] - df["operational_cost"]

df.fillna(df.mean(numeric_only=True), inplace=True)

engine = create_engine("sqlite:///../plantation.db")
df.to_sql("plantation_cleaned", engine, if_exists="replace", index=False)

print("✅ ETL pipeline completed")
