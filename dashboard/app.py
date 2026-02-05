import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(page_title="Plantation Analytics Dashboard", layout="wide")

st.title("🌱 Plantation Analytics Dashboard")
# LOAD DATA
engine = create_engine('sqlite:///plantation.db')

df = pd.read_sql("SELECT * FROM plantation", engine)

df["date"]= pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)
df["profit_margin"]= df["profit"] / df["operational_cost"]

# UPGRADE-- KPI CARDS
st.header("Key Metrics")

col1, col2, col3 = st.columns(3)

total_rofit = df["profit"].sum()
avg_margin = df["profit_margin"].mean()
total_production = df["production_ton"].sum()
col1.metric("Total Profit", f"${total_rofit:,.2f}")
col2.metric("Average Profit Margin", f"{avg_margin:.2%}")
col3.metric("Total Production (tons)", f"{total_production:,.2f}")

# KPI growth indicator
monthly = df.groupby("month")["profit"].sum()

growth = ((monthly.iloc[-1] - monthly.iloc[-2]) / monthly.iloc[-2]) * 100

st.metric("MoM Growth", f"{growth:.2f}%", delta=f"{growth:.2f}%")


# UPGRADE -- Executive Summary Insight
best_region = df.groupby("region")["profit"].sum().idxmax()
worst_region = df.groupby("region")["profit"].sum().idxmin()

trend = "increasing" if df.groupby("month")["profit"].sum().iloc[-1] > df.groupby("month")["profit"].sum().iloc[0] else "declining"

st.subheader("Executive Insight")

st.write(f"""
📌 Best performing region: **{best_region}**  
⚠ Region needing attention: **{worst_region}**  
📈 Overall trend: **{trend}**

Operational efficiency remains a key driver of profitability.
""")

# UPGRADE -- Side Bar Filter Region
st.sidebar.header("Filters")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df["region"].unique(),
    default=df["region"].unique()
)

df = df[df["region"].isin(region_filter)]

# Upgrade 3 — Date Range Filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["date"].min(), df["date"].max()]
)

df = df[
    (df["date"] >= pd.to_datetime(date_range[0])) &
    (df["date"] <= pd.to_datetime(date_range[1]))
]
# CHART1--TOTAL PRIFIT BY REGION
st.header("Total Profit by Region")

region_profit = df.groupby("region")["profit"].sum().reset_index()

fig1 = px.bar(region_profit, x="region", y="profit", title="Total Profit by Region")
st.plotly_chart(fig1, width='stretch')

# CHART2--Monthly Trend
st.header("Monthly Profit Trend")

monthly_profit = df.groupby("month")["profit"].sum().reset_index()

fig2 = px.line(monthly_profit, x="month", y="profit", title="Monthly Profit Trend")
st.plotly_chart(fig2, width='stretch')

# CHART3--DISTRIBUTIOM
st.header("Profit Distribution")

fig3 = px.histogram(df, x="profit", nbins=30, title="Profit Distribution")
st.plotly_chart(fig3, width='stretch')

# CHART4 -- Correlation Heatmap
st.header("Correlation Heatmap")

corr = df.corr(numeric_only=True)

fig4 = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
st.plotly_chart(fig4, width='stretch')

# CHART5--REGION TREND
st.header("Profit Trend by Region")

region_month = df.groupby(["month","region"])["profit"].sum().reset_index()

fig5 = px.line(region_month, x="month", y="profit", color="region",
               title="Profit Trend by Region")
st.plotly_chart(fig5, width='stretch')

