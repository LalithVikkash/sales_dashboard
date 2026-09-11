# Sales Performance & Profitability Dashboard

An interactive business analytics dashboard built with Python, Pandas, NumPy, SQL, SQLite, and Streamlit to analyze sales performance, profitability, products, categories, and regional trends.

## Dashboard Preview

The dashboard provides an interactive view of key sales and profitability metrics with filters for region and category.

## Features

- Interactive region and category filters
- Total sales and total profit KPIs
- Order and quantity tracking
- Profit margin calculation
- Monthly sales trend visualization
- Top products by sales
- Regional sales analysis
- Category-level performance analysis
- Product profitability analysis
- Detailed sales data exploration
- SQL-based category performance analysis

## Tech Stack

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Database:** SQLite
- **Querying:** SQL
- **Dashboard:** Streamlit

## Dataset

The project uses a sample sales dataset containing:

- Order date
- Product
- Category
- Region
- Quantity
- Sales
- Cost
- Profit

The dataset contains 500 sales records generated for analysis and dashboard demonstration.

## SQL Analysis

The sales data is loaded into a SQLite database and analyzed using SQL queries.

The SQL analysis includes:

- Total sales by category
- Total profit by category
- Total quantity sold by category
- Category ranking based on sales performance

## Project Structure

```text
sales_dashboard/
├── app.py
├── sales_data.csv
├── requirements.txt
├── README.md
└── .gitignore