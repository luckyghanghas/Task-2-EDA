# Task 2: Exploratory Data Analysis & Business Intelligence

This repository contains the Task 2 submission for the 60-day Data Analytics internship. It builds on the cleaned dataset from Task 1 and focuses on exploratory data analysis, SQL-based business questions, and a static dashboard mock-up.

## Objective

Uncover patterns, trends, and business insights from the cleaned sales dataset using descriptive statistics, SQL queries, and dashboard-style KPI reporting.

## Repository Structure

```text
data/
  sales_transactions_cleaned.csv
dashboard/
  sales_dashboard_mockup.xlsx
  dashboard_summary.json
reports/
  eda_report.md
  sql_query_results.md
  linkedin_video_script.md
scripts/
  task2_analysis.py
sql/
  business_questions.sql
requirements.txt
```

## Business Questions Answered

1. What are the top 5 products by completed-order revenue?
2. What is the monthly revenue trend?
3. Which regions generate the highest revenue?
4. Which sales channels perform best?
5. Which customer segments contribute the most revenue?
6. Which products have the highest return and cancellation rates?
7. Which payment modes contribute the most completed-order revenue?

## Deliverables

- EDA report: `reports/eda_report.md`
- SQL queries: `sql/business_questions.sql`
- SQL query results: `reports/sql_query_results.md`
- Static dashboard mock-up: `dashboard/sales_dashboard_mockup.xlsx`
- LinkedIn video script: `reports/linkedin_video_script.md`

## How to Run

```bash
pip install -r requirements.txt
python scripts/task2_analysis.py
```

## Key Insights

The analysis identifies revenue trends, top products, regional performance, sales-channel performance, customer-segment revenue, and return/cancellation behavior. These outputs define the most important KPIs for the dashboard and prepare the project for deeper analysis in Task 3.
