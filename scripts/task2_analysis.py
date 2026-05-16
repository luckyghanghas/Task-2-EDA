from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sales_transactions_cleaned.csv"
SQL_PATH = ROOT / "sql" / "business_questions.sql"
SQL_RESULTS_PATH = ROOT / "reports" / "sql_query_results.md"
EDA_REPORT_PATH = ROOT / "reports" / "eda_report.md"
SUMMARY_JSON_PATH = ROOT / "dashboard" / "dashboard_summary.json"


def money(value: float) -> str:
    return f"Rs. {value:,.2f}"


def markdown_table(df: pd.DataFrame, max_rows: int = 10) -> str:
    table = df.head(max_rows).copy()
    headers = [str(col) for col in table.columns]
    rows = [[str(value) for value in row] for row in table.to_numpy()]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(lines)


def main() -> None:
    df = pd.read_csv(DATA_PATH, parse_dates=["order_date", "customer_dob"])
    completed = df[df["order_status"] == "Completed"].copy()

    total_orders = int(len(df))
    completed_orders = int(len(completed))
    total_revenue = float(completed["net_revenue"].sum())
    avg_order_value = float(completed["net_revenue"].mean())
    return_rate = float((df["order_status"] == "Returned").mean())
    cancel_rate = float((df["order_status"] == "Cancelled").mean())
    top_product = completed.groupby("product")["net_revenue"].sum().idxmax()
    top_region = completed.groupby("region")["net_revenue"].sum().idxmax()

    monthly_revenue = (
        completed.groupby("order_month", as_index=False)["net_revenue"]
        .sum()
        .sort_values("order_month")
        .rename(columns={"net_revenue": "revenue"})
    )
    product_revenue = (
        completed.groupby("product", as_index=False)
        .agg(revenue=("net_revenue", "sum"), orders=("order_id", "count"), units=("quantity", "sum"))
        .sort_values("revenue", ascending=False)
    )
    region_revenue = (
        completed.groupby("region", as_index=False)
        .agg(revenue=("net_revenue", "sum"), orders=("order_id", "count"))
        .sort_values("revenue", ascending=False)
    )
    channel_revenue = (
        completed.groupby("sales_channel", as_index=False)
        .agg(revenue=("net_revenue", "sum"), orders=("order_id", "count"))
        .sort_values("revenue", ascending=False)
    )
    segment_revenue = (
        completed.groupby("customer_segment", as_index=False)
        .agg(revenue=("net_revenue", "sum"), avg_order_value=("net_revenue", "mean"), orders=("order_id", "count"))
        .sort_values("revenue", ascending=False)
    )

    numeric_summary = df[["quantity", "unit_price", "discount_rate", "gross_revenue", "net_revenue", "customer_age"]].describe().round(2)
    categorical_summary = {
        "product_count": int(df["product"].nunique()),
        "region_count": int(df["region"].nunique()),
        "sales_channel_count": int(df["sales_channel"].nunique()),
        "customer_segment_count": int(df["customer_segment"].nunique()),
        "payment_mode_count": int(df["payment_mode"].nunique()),
    }
    correlation = df[["quantity", "unit_price", "discount_rate", "customer_age", "net_revenue"]].corr(numeric_only=True).round(3)

    EDA_REPORT_PATH.write_text(
        "\n".join(
            [
                "# Exploratory Data Analysis Report",
                "",
                "## Executive Summary",
                f"- Total records analyzed: {total_orders}",
                f"- Completed orders: {completed_orders}",
                f"- Completed-order revenue: {money(total_revenue)}",
                f"- Average order value: {money(avg_order_value)}",
                f"- Return rate: {return_rate:.1%}",
                f"- Cancellation rate: {cancel_rate:.1%}",
                f"- Top product by revenue: {top_product}",
                f"- Top region by revenue: {top_region}",
                "",
                "## Descriptive Statistics",
                markdown_table(numeric_summary.reset_index().rename(columns={"index": "metric"}), 20),
                "",
                "## Categorical Profile",
                *[f"- {key.replace('_', ' ').title()}: {value}" for key, value in categorical_summary.items()],
                "",
                "## Monthly Revenue Trend",
                markdown_table(monthly_revenue),
                "",
                "## Top Products by Revenue",
                markdown_table(product_revenue),
                "",
                "## Revenue by Region",
                markdown_table(region_revenue),
                "",
                "## Revenue by Sales Channel",
                markdown_table(channel_revenue),
                "",
                "## Revenue by Customer Segment",
                markdown_table(segment_revenue),
                "",
                "## Correlation Matrix",
                markdown_table(correlation.reset_index().rename(columns={"index": "field"}), 20),
                "",
                "## Key Insights",
                f"- {top_product} generated the highest completed-order revenue.",
                f"- {top_region} was the strongest region by revenue.",
                "- Sales performance should be monitored monthly because revenue varies by order month.",
                "- Product, region, channel, and segment cuts provide useful dashboard dimensions for business users.",
                "- Return and cancellation rates should be tracked because they reduce realized sales impact.",
                "",
                "## Recommended KPIs for Dashboard",
                "- Completed-order revenue",
                "- Average order value",
                "- Completed orders",
                "- Return rate",
                "- Cancellation rate",
                "- Revenue by month, product, region, channel, and customer segment",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    queries = {
        "top_5_products_by_revenue": """
SELECT product, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS completed_orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY product
ORDER BY revenue DESC
LIMIT 5;
""",
        "monthly_revenue_trend": """
SELECT order_month, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS completed_orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY order_month
ORDER BY order_month;
""",
        "revenue_by_region": """
SELECT region, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS completed_orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY region
ORDER BY revenue DESC;
""",
        "sales_channel_performance": """
SELECT sales_channel, ROUND(SUM(net_revenue), 2) AS revenue, ROUND(AVG(net_revenue), 2) AS avg_order_value
FROM sales
WHERE order_status = 'Completed'
GROUP BY sales_channel
ORDER BY revenue DESC;
""",
        "customer_segment_performance": """
SELECT customer_segment, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(DISTINCT customer_id) AS customers
FROM sales
WHERE order_status = 'Completed'
GROUP BY customer_segment
ORDER BY revenue DESC;
""",
        "return_and_cancellation_by_product": """
SELECT product,
       ROUND(AVG(CASE WHEN order_status = 'Returned' THEN 1.0 ELSE 0 END) * 100, 2) AS return_rate_pct,
       ROUND(AVG(CASE WHEN order_status = 'Cancelled' THEN 1.0 ELSE 0 END) * 100, 2) AS cancellation_rate_pct
FROM sales
GROUP BY product
ORDER BY return_rate_pct DESC, cancellation_rate_pct DESC;
""",
        "payment_mode_revenue": """
SELECT payment_mode, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY payment_mode
ORDER BY revenue DESC;
""",
    }

    SQL_PATH.write_text(
        "\n".join([f"-- {name}\n{query.strip()}\n" for name, query in queries.items()]),
        encoding="utf-8",
    )

    con = sqlite3.connect(":memory:")
    df.to_sql("sales", con, index=False, if_exists="replace")
    result_sections = ["# SQL Query Results", ""]
    dashboard_sql_results = {}
    for name, query in queries.items():
        result = pd.read_sql_query(query, con)
        dashboard_sql_results[name] = result.to_dict(orient="records")
        result_sections.extend([f"## {name.replace('_', ' ').title()}", "", "```sql", query.strip(), "```", "", markdown_table(result, 20), ""])
    SQL_RESULTS_PATH.write_text("\n".join(result_sections), encoding="utf-8")

    summary = {
        "kpis": {
            "total_orders": total_orders,
            "completed_orders": completed_orders,
            "total_revenue": round(total_revenue, 2),
            "avg_order_value": round(avg_order_value, 2),
            "return_rate": round(return_rate, 4),
            "cancel_rate": round(cancel_rate, 4),
        },
        "monthly_revenue": monthly_revenue.round(2).to_dict(orient="records"),
        "product_revenue": product_revenue.round(2).to_dict(orient="records"),
        "region_revenue": region_revenue.round(2).to_dict(orient="records"),
        "channel_revenue": channel_revenue.round(2).to_dict(orient="records"),
        "segment_revenue": segment_revenue.round(2).to_dict(orient="records"),
        "sql_results": dashboard_sql_results,
    }
    SUMMARY_JSON_PATH.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"Wrote {EDA_REPORT_PATH}")
    print(f"Wrote {SQL_PATH}")
    print(f"Wrote {SQL_RESULTS_PATH}")
    print(f"Wrote {SUMMARY_JSON_PATH}")


if __name__ == "__main__":
    main()
