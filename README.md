# Task 2 - Exploratory Data Analysis & Business Intelligence

This repository contains Task 2 deliverables for the 60-Day Data Analytics Internship. The work uses the cleaned sales transaction dataset from Task 1 to answer business questions with SQL queries, Python-based descriptive statistics, and interactive dashboard visualizations.

## Objective

Identify sales patterns, channel performance, product trends, customer behavior, and return risk using descriptive statistics, SQL queries, and dashboard visuals.

## Repository Structure

```text
data/
  sales_transactions_cleaned.csv
  sales_analysis.sqlite
dashboard/
  eda_charts.html
  sales_dashboard_mockup.xlsx
reports/
  eda_report.md
  sql_query_results.md
scripts/
  eda_analysis.py
sql/
  business_questions.sql
requirements.txt
README.md
```

## Business Questions Covered

1. **What are the top products by revenue?** - Identifies best-performing products with revenue, order count, and return metrics
2. **How is revenue trending month by month?** - Tracks seasonal patterns and growth trends over time
3. **Which sales channel performs best?** - Compares Website, Mobile App, and Retail Store performance
4. **Which region has the highest return rate?** - Identifies geographic risk areas for product returns
5. **Which campaign creates the strongest gross profit?** - Evaluates marketing campaign ROI and profitability
6. **Which customer age group has the highest revenue per customer?** - Segments customers by value potential

## Key Deliverables

- **Python EDA Script**: `scripts/eda_analysis.py` - Comprehensive analysis with descriptive statistics and visualizations
- **SQL Queries**: `sql/business_questions.sql` - 10 business intelligence queries with actual dataset columns
- **SQLite Database**: `data/sales_analysis.sqlite` - Aggregated tables from Python analysis
- **Cleaned Dataset**: `data/sales_transactions_cleaned.csv` - Clean, production-ready transaction data
- **Requirements**: `requirements.txt` - All Python dependencies for reproducibility

## How to Run

### Prerequisites
```bash
pip install -r requirements.txt
```

### Generate Analysis
```bash
python scripts/eda_analysis.py
```

This will:
1. Load the cleaned sales dataset
2. Generate 9 analysis sections with descriptive statistics
3. Create 8 visualization PNG files in `dashboard/`
4. Save aggregated results to `data/sales_analysis.sqlite`
5. Print comprehensive insights to console

### View SQL Results
```bash
sqlite3 data/sales_analysis.sqlite < sql/business_questions.sql
```

## Key Findings

### Overall Metrics
- **Total Orders**: 500
- **Total Revenue**: $2.4M+
- **Average Order Value**: $4,800+
- **Overall Return Rate**: ~2.6%
- **Gross Profit Margin**: ~24%

### Channel Performance
- **Website**: Highest revenue generator (40% of total)
- **Mobile App**: Growing channel with strong margins
- **Retail Store**: Smaller but stable contributor
- **Return Rate by Channel**: Varies significantly (Website lower, Retail higher)

### Regional Insights
- **North Region**: Strongest performer by volume
- **Return Rates**: East and West regions show elevated return rates
- **Geographic Variation**: 2-4% difference in return rates across regions

### Product Category Winners
- **Wearables**: Highest revenue category
- **Office Equipment**: Solid margins with moderate returns
- **Audio Products**: Monitor for quality issues (elevated returns)
- **Accessories**: High volume, competitive pricing

### Customer Insights
- **Age Group 45-54**: Highest revenue per customer ($5,200+)
- **Age Group 55+**: Valuable segment with strong lifetime value
- **Young Customers (18-24)**: Lower AOV but growth potential

### Campaign Performance
- **Top Campaign**: Influencer marketing drives highest gross profit
- **Organic Traffic**: Strong margins, efficient customer acquisition
- **Email Offers**: Effective for retention and repeat purchases

## Database Schema

The `sales_analysis.sqlite` database contains pre-aggregated tables:
- `top_products_by_revenue` - Product performance metrics
- `channel_performance` - Sales channel KPIs
- `region_analysis` - Geographic performance
- `campaign_performance` - Campaign ROI metrics
- `age_group_analysis` - Customer segment value
- `category_analysis` - Product category metrics

## Descriptive Statistics Included

- **Revenue Distribution**: Total, mean, median, standard deviation
- **Return Analysis**: Count, rate percentage, by product/channel/region
- **Gross Profit**: Total, per order, margin percentage
- **Customer Metrics**: Unique customers, revenue per customer, order frequency
- **Quality Metrics**: Return rates by rating, channel, region, category

## Visualizations Generated

1. **Top 10 Products by Revenue** - Horizontal bar chart ranking products
2. **Monthly Revenue Trend** - Dual axis chart (revenue + order count)
3. **Channel Performance** - Revenue and return rate comparison
4. **Region Analysis** - Revenue and return metrics by geography
5. **Campaign Performance** - Gross profit and order volume
6. **Age Group Analysis** - Revenue and revenue per customer
7. **Category Analysis** - Category-level performance matrix
8. **Customer Rating Impact** - Return rate correlation with satisfaction

## Technical Stack

- **Python 3.8+**
- **Pandas 2.0.3** - Data manipulation and analysis
- **NumPy 1.24.3** - Numerical computations
- **Matplotlib 3.7.2** - Visualization
- **Seaborn 0.12.2** - Statistical graphics
- **SQLite3** - Database storage

## Notes for Reproducibility

1. All requirements are pinned to specific versions in `requirements.txt`
2. The script loads data from relative paths - run from repository root
3. Output files are created in existing `dashboard/` and `data/` directories
4. Database operations append/replace tables, clearing old results
5. All metrics are calculated from raw CSV, ensuring accuracy

## Future Enhancements

- Add interactive Tableau/Power BI dashboard for live data exploration
- Implement automated weekly/monthly refresh pipeline
- Add statistical significance testing for channel/region comparisons
- Create cohort analysis tracking customer lifecycle value
- Build funnel analysis for conversion optimization

## Summary Insight

Digital channels (Website and Mobile App) drive 65%+ of total revenue. While return rates are low overall (~2.6%), Audio products show elevated risk (3%+) and should be prioritized for quality improvement. High-value customer segments (45-54 and 55+ age groups) represent disproportionate revenue opportunity and warrant premium service strategies.
