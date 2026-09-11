import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Performance & Profitability Dashboard")
st.write("Analyze sales, profit, orders, products, and regional performance.")

df = pd.read_csv("sales_data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories))
]

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = len(filtered_df)
total_quantity = filtered_df["Quantity"].sum()

profit_margin = (
    (total_profit / total_sales) * 100
    if total_sales > 0 else 0
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Sales", f"₹{total_sales:,.0f}")
col2.metric("Total Profit", f"₹{total_profit:,.0f}")
col3.metric("Orders", f"{total_orders:,}")
col4.metric("Quantity Sold", f"{total_quantity:,}")
col5.metric("Profit Margin", f"{profit_margin:.2f}%")

st.divider()

st.subheader("📈 Monthly Sales Trend")

monthly_sales = (
    filtered_df
    .set_index("Order_Date")
    .resample("ME")["Sales"]
    .sum()
)

st.line_chart(monthly_sales)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top Products by Sales")

    top_products = (
        filtered_df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(top_products)

with col2:
    st.subheader("🌍 Sales by Region")

    region_sales = (
        filtered_df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(region_sales)

st.subheader("📦 Category Performance")

category_performance = (
    filtered_df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
)

st.dataframe(
    category_performance.style.format({
        "Sales": "₹{:,.0f}",
        "Profit": "₹{:,.0f}",
        "Quantity": "{:,.0f}"
    }),
    use_container_width=True
)

st.subheader("💰 Product Profitability")

product_profit = (
    filtered_df.groupby("Product")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Profit", ascending=False)
)

st.dataframe(
    product_profit.style.format({
        "Sales": "₹{:,.0f}",
        "Profit": "₹{:,.0f}"
    }),
    use_container_width=True
)

st.subheader("🔎 Sales Data")

st.dataframe(
    filtered_df.sort_values("Order_Date", ascending=False),
    use_container_width=True
)

conn = sqlite3.connect("sales_dashboard.db")
filtered_df.to_sql("sales", conn, if_exists="replace", index=False)

query = """
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC
"""

sql_result = pd.read_sql_query(query, conn)
conn.close()

st.subheader("🗄️ SQL Analysis")

st.dataframe(
    sql_result.style.format({
        "Total_Sales": "₹{:,.0f}",
        "Total_Profit": "₹{:,.0f}",
        "Total_Quantity": "{:,.0f}"
    }),
    use_container_width=True
)

st.caption("Built with Python, Pandas, NumPy, SQL, SQLite, and Streamlit.")