# Task 2 - Exploratory Data Analysis & Business Intelligence

This repository contains Task 2 deliverables for the 60-Day Data Analytics Internship at **ApexPlanet Software Pvt. Ltd.** The work uses the cleaned sales transaction dataset from Task 1 to answer six business questions using SQL queries, Python-based descriptive statistics, and interactive dashboard visualizations.

---

## Objective

Identify sales patterns, channel performance, product trends, customer behavior, and return risk using descriptive statistics, SQL queries, and dashboard visuals.

---

## Repository Structure

```
data/
  sales_transactions_cleaned.csv   # 1,250 cleaned transactions
  sales_analysis.sqlite            # SQLite DB with aggregated tables
dashboard/
  eda_charts.html                  # Static SVG bar charts
  sales_dashboard_mockup.xlsx      # Excel dashboard with 6 embedded charts
reports/
  eda_report.md                    # Full EDA report with findings and insights
  sql_query_results.md             # All 6 query results with actual numbers
scripts/
  eda_analysis.py                  # Python EDA script
sql/
  business_questions.sql           # 6 SQL queries with insights
requirements.txt
README.md
```

---

## Business Questions Covered

1. **Top products by revenue** — Identifies best-performing products with revenue, order count, and return metrics
2. **Monthly revenue trend** — Tracks seasonal patterns and growth trends over 15 months (Jan 2025 – Mar 2026)
3. **Sales channel performance** — Compares Website, Mobile App, and Retail Store on revenue, margin, and returns
4. **Region return rate** — Identifies geographic risk areas for product returns
5. **Campaign ROI** — Evaluates marketing campaign gross margin and profitability
6. **Customer age group value** — Segments customers by revenue per customer

---

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
1. Load the cleaned sales dataset (1,250 rows)
2. Generate 9 analysis sections with descriptive statistics
3. Create 8 visualization PNG files in `dashboard/`
4. Save aggregated results to `data/sales_analysis.sqlite`
5. Print comprehensive insights to console

### View SQL Results
```bash
sqlite3 data/sales_analysis.sqlite < sql/business_questions.sql
```

---

## Key Findings (Verified from 1,250-row Dataset)

### Overall Metrics

| Metric | Value |
|---|---|
| Total Orders | **1,250** |
| Total Revenue | **$5,328,492.40** |
| Average Order Value | **$4,262.79** |
| Gross Margin | **20.32%** |
| Return Rate | **5.20%** |
| Average Customer Rating | **3.83 / 5** |
| Date Range | **Jan 2025 – Mar 2026 (15 months)** |

---

### Top Products by Revenue

| Product | Revenue | Orders | Return Rate |
|---|---|---|---|
| Smart Watch | $1,368,210 | 152 | 7.24% |
| Mechanical Keyboard | $899,190 | 156 | 1.28% ✅ |
| Webcam Pro | $798,138 | 169 | 4.73% |
| Bluetooth Headphones | $655,422 | 151 | 5.30% |
| Portable Speaker | $600,264 | 157 | 7.64% |
| USB-C Hub | $506,904 | 161 | 6.83% |
| Laptop Stand | $296,637 | 143 | 4.90% |
| Wireless Mouse | $203,728 | 161 | 3.73% |

---

### Channel Performance

| Channel | Revenue | Orders | Gross Margin |
|---|---|---|---|
| Website | $2,464,280 | 592 | 19.84% |
| Mobile App | $2,054,499 | 456 | 21.49% ✅ |
| Retail Store | $809,714 | 202 | 18.81% |

**Finding:** Website leads volume (46.2% share). Mobile App leads profitability at 21.49% margin. Digital channels together = 84.8% of revenue.

---

### Regional Performance

| Region | Revenue | Orders | Return Rate |
|---|---|---|---|
| West | $1,451,299 | 339 | 3.83% ✅ |
| South | $1,301,485 | 320 | 7.19% ⚠️ |
| North | $1,288,065 | 299 | 5.69% |
| East | $1,287,644 | 292 | 4.11% |

**Finding:** South region return rate (7.19%) is 88% higher than West (3.83%) — requires investigation.

---

### Campaign ROI

| Campaign | Revenue | Gross Profit | Margin |
|---|---|---|---|
| Search Ads | $1,034,918 | $276,020 | 26.67% ✅ |
| Organic | $946,146 | $198,462 | 20.98% |
| Referral | $904,176 | $185,195 | 20.48% |
| Influencer | $809,556 | $158,624 | 19.59% |
| Festive Sale | $789,240 | $147,123 | 18.64% |
| Email Offer | $844,456 | $117,325 | 13.89% ⚠️ |

**Finding:** Search Ads delivers the highest margin at 26.67%. Email Offer at 13.89% is destroying profit with heavy discounting.

---

### Customer Age Segment Value

| Age Group | Customers | Revenue | Rev/Customer |
|---|---|---|---|
| 55+ | 184 | $1,145,018 | $6,222.92 ✅ |
| 35–44 | 201 | $1,206,868 | $6,004.32 |
| 18–24 | 154 | $884,965 | $5,746.53 |
| 25–34 | 183 | $1,032,053 | $5,639.63 |
| 45–54 | 201 | $1,059,588 | $5,271.58 |

**Finding:** 55+ customers have the highest revenue per customer at $6,222.92 — a high-value, underserved segment.

---

## Key Strategic Insights

1. **Double down on digital** — Website + Mobile App = 84.8% of revenue. Digital-first investment is justified.
2. **Fix the South region return problem** — 7.19% vs 3.83% for West. Investigate delivery SLAs and product mix.
3. **Reallocate Email Offer budget to Search Ads** — 12.78pp margin gap means ~$100K annual gross profit upside.
4. **Target 55+ and 35–44 segments** — highest revenue per customer. Loyalty and premium campaigns would yield strong ROI.
5. **Smart Watch needs attention** — Top revenue product ($1.37M) but 7.24% return rate signals expectation gap.

---

## Database Schema

The `sales_analysis.sqlite` database contains pre-aggregated tables:
- `top_products_by_revenue` — Product performance metrics
- `channel_performance` — Sales channel KPIs
- `region_analysis` — Geographic performance
- `campaign_performance` — Campaign ROI metrics
- `age_group_analysis` — Customer segment value
- `category_analysis` — Product category metrics

---

## Technical Stack

- **Python 3.8+**
- **Pandas 2.0.3** — Data manipulation and analysis
- **NumPy 1.24.3** — Numerical computations
- **Matplotlib 3.7.2** — Visualization
- **Seaborn 0.12.2** — Statistical graphics
- **SQLite3** — Database storage
- **openpyxl** — Excel dashboard generation

---

## Related Repositories

- [Task-1-Data-Immersion-Wrangling](https://github.com/luckyghanghas/Task-1-Data-Immersion-Wrangling) — Source cleaned dataset
- [Task-3-Dashboard](https://github.com/luckyghanghas/Task-3-Dashboard) — Deep-dive dashboarding
- [Task-4-Storytelling](https://github.com/luckyghanghas/Task-4-Storytelling) — Statistical validation
- [Portfolio](https://github.com/luckyghanghas/Lucky-DataAnalyst-Internship-Portfolio) — Master portfolio