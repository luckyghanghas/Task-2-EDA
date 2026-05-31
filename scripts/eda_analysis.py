"""
Task 2 - EDA & Business Intelligence Analysis
Exploratory Data Analysis using Pandas, NumPy, and Visualization Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from datetime import datetime

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Load dataset
df = pd.read_csv('data/sales_transactions_cleaned.csv')

print("="*80)
print("TASK 2 - EXPLORATORY DATA ANALYSIS & BUSINESS INTELLIGENCE")
print("="*80)
print(f"\nDataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"Date Range: {df['order_date'].min()} to {df['order_date'].max()}")

# ============================================================================
# 1. DESCRIPTIVE STATISTICS
# ============================================================================
print("\n" + "="*80)
print("1. DESCRIPTIVE STATISTICS")
print("="*80)

print("\n--- Numeric Column Summary ---")
numeric_cols = df.select_dtypes(include=[np.number]).columns
print(df[numeric_cols].describe().round(2))

print("\n--- Revenue Distribution ---")
print(f"Total Revenue: ${df['revenue'].sum():,.2f}")
print(f"Mean Order Value (MOV): ${df['revenue'].mean():,.2f}")
print(f"Median Revenue: ${df['revenue'].median():,.2f}")
print(f"Revenue Std Dev: ${df['revenue'].std():,.2f}")

print("\n--- Return Rate Analysis ---")
return_rate = (df['returned'].sum() / len(df)) * 100
print(f"Overall Return Rate: {return_rate:.2f}%")
print(f"Total Returns: {df['returned'].sum()}")
print(f"Total Orders: {len(df)}")

print("\n--- Gross Profit Analysis ---")
df['gross_profit'] = df['revenue'] - df['cost']
print(f"Total Gross Profit: ${df['gross_profit'].sum():,.2f}")
print(f"Mean Gross Profit per Order: ${df['gross_profit'].mean():,.2f}")
print(f"Gross Profit Margin: {(df['gross_profit'].sum() / df['revenue'].sum() * 100):.2f}%")

# ============================================================================
# 2. BUSINESS QUESTION 1: TOP PRODUCTS BY REVENUE
# ============================================================================
print("\n" + "="*80)
print("2. BUSINESS QUESTION 1: TOP PRODUCTS BY REVENUE")
print("="*80)

top_products = df.groupby('product_name').agg({
    'revenue': ['sum', 'count', 'mean'],
    'returned': 'sum'
}).round(2)
top_products.columns = ['Total Revenue', 'Order Count', 'Avg Order Value', 'Returns']
top_products['Return Rate %'] = (top_products['Returns'] / top_products['Order Count'] * 100).round(2)
top_products = top_products.sort_values('Total Revenue', ascending=False)
print(top_products)

# Visualization
fig, ax = plt.subplots(figsize=(12, 6))
top_10_products = df.groupby('product_name')['revenue'].sum().nlargest(10)
top_10_products.plot(kind='barh', ax=ax, color='steelblue')
ax.set_xlabel('Total Revenue ($)')
ax.set_title('Top 10 Products by Revenue')
plt.tight_layout()
plt.savefig('dashboard/top_products_by_revenue.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 3. BUSINESS QUESTION 2: REVENUE TRENDING MONTH BY MONTH
# ============================================================================
print("\n" + "="*80)
print("3. BUSINESS QUESTION 2: REVENUE TRENDING MONTH BY MONTH")
print("="*80)

df['order_date'] = pd.to_datetime(df['order_date'])
df['year_month'] = df['order_date'].dt.to_period('M')
monthly_revenue = df.groupby('year_month').agg({
    'revenue': 'sum',
    'order_id': 'count'
}).round(2)
monthly_revenue.columns = ['Total Revenue', 'Order Count']
monthly_revenue['Avg Order Value'] = (monthly_revenue['Total Revenue'] / monthly_revenue['Order Count']).round(2)
print(monthly_revenue)

# Visualization
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8))
monthly_revenue['Total Revenue'].plot(kind='line', ax=ax1, marker='o', linewidth=2, color='green')
ax1.set_title('Monthly Revenue Trend')
ax1.set_ylabel('Revenue ($)')
ax1.grid(True, alpha=0.3)

monthly_revenue['Order Count'].plot(kind='bar', ax=ax2, color='coral')
ax2.set_title('Monthly Order Volume')
ax2.set_ylabel('Number of Orders')
ax2.set_xlabel('Month')
plt.tight_layout()
plt.savefig('dashboard/revenue_trending.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 4. BUSINESS QUESTION 3: SALES CHANNEL PERFORMANCE
# ============================================================================
print("\n" + "="*80)
print("4. BUSINESS QUESTION 3: WHICH SALES CHANNEL PERFORMS BEST?")
print("="*80)

channel_performance = df.groupby('sales_channel').agg({
    'revenue': ['sum', 'count', 'mean'],
    'gross_profit': 'sum',
    'returned': 'sum'
}).round(2)
channel_performance.columns = ['Total Revenue', 'Order Count', 'Avg Order Value', 'Gross Profit', 'Returns']
channel_performance['Return Rate %'] = (channel_performance['Returns'] / channel_performance['Order Count'] * 100).round(2)
channel_performance['Profit Margin %'] = (channel_performance['Gross Profit'] / channel_performance['Total Revenue'] * 100).round(2)
channel_performance = channel_performance.sort_values('Total Revenue', ascending=False)
print(channel_performance)

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
df.groupby('sales_channel')['revenue'].sum().plot(kind='bar', ax=axes[0], color='steelblue')
axes[0].set_title('Revenue by Sales Channel')
axes[0].set_ylabel('Total Revenue ($)')
axes[0].set_xlabel('Sales Channel')

return_by_channel = (df.groupby('sales_channel')['returned'].sum() / df.groupby('sales_channel').size() * 100)
return_by_channel.plot(kind='bar', ax=axes[1], color='red')
axes[1].set_title('Return Rate by Sales Channel')
axes[1].set_ylabel('Return Rate (%)')
axes[1].set_xlabel('Sales Channel')
plt.tight_layout()
plt.savefig('dashboard/channel_performance.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 5. BUSINESS QUESTION 4: REGION ANALYSIS - RETURN RATE & REVENUE
# ============================================================================
print("\n" + "="*80)
print("5. BUSINESS QUESTION 4: REGION ANALYSIS - RETURN RATE & REVENUE")
print("="*80)

region_analysis = df.groupby('region').agg({
    'revenue': ['sum', 'count', 'mean'],
    'gross_profit': 'sum',
    'returned': 'sum'
}).round(2)
region_analysis.columns = ['Total Revenue', 'Order Count', 'Avg Order Value', 'Gross Profit', 'Returns']
region_analysis['Return Rate %'] = (region_analysis['Returns'] / region_analysis['Order Count'] * 100).round(2)
region_analysis = region_analysis.sort_values('Total Revenue', ascending=False)
print(region_analysis)

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
df.groupby('region')['revenue'].sum().sort_values(ascending=False).plot(kind='bar', ax=axes[0], color='teal')
axes[0].set_title('Revenue by Region')
axes[0].set_ylabel('Total Revenue ($)')
axes[0].set_xlabel('Region')

return_by_region = (df.groupby('region')['returned'].sum() / df.groupby('region').size() * 100).sort_values(ascending=False)
return_by_region.plot(kind='bar', ax=axes[1], color='orange')
axes[1].set_title('Return Rate by Region')
axes[1].set_ylabel('Return Rate (%)')
axes[1].set_xlabel('Region')
plt.tight_layout()
plt.savefig('dashboard/region_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 6. BUSINESS QUESTION 5: CAMPAIGN PERFORMANCE - GROSS PROFIT
# ============================================================================
print("\n" + "="*80)
print("6. BUSINESS QUESTION 5: CAMPAIGN PERFORMANCE - GROSS PROFIT")
print("="*80)

campaign_performance = df.groupby('campaign').agg({
    'revenue': ['sum', 'count', 'mean'],
    'gross_profit': 'sum',
    'returned': 'sum'
}).round(2)
campaign_performance.columns = ['Total Revenue', 'Order Count', 'Avg Order Value', 'Gross Profit', 'Returns']
campaign_performance['Profit Margin %'] = (campaign_performance['Gross Profit'] / campaign_performance['Total Revenue'] * 100).round(2)
campaign_performance['Return Rate %'] = (campaign_performance['Returns'] / campaign_performance['Order Count'] * 100).round(2)
campaign_performance = campaign_performance.sort_values('Gross Profit', ascending=False)
print(campaign_performance)

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
df.groupby('campaign')['gross_profit'].sum().sort_values(ascending=False).plot(kind='bar', ax=axes[0], color='darkgreen')
axes[0].set_title('Gross Profit by Campaign')
axes[0].set_ylabel('Gross Profit ($)')
axes[0].set_xlabel('Campaign')

df.groupby('campaign').size().sort_values(ascending=False).plot(kind='bar', ax=axes[1], color='purple')
axes[1].set_title('Order Volume by Campaign')
axes[1].set_ylabel('Number of Orders')
axes[1].set_xlabel('Campaign')
plt.tight_layout()
plt.savefig('dashboard/campaign_performance.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 7. BUSINESS QUESTION 6: CUSTOMER AGE GROUP ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("7. BUSINESS QUESTION 6: CUSTOMER AGE GROUP ANALYSIS")
print("="*80)

age_analysis = df.groupby('age_group').agg({
    'revenue': ['sum', 'count', 'mean'],
    'customer_id': 'nunique',
    'returned': 'sum'
}).round(2)
age_analysis.columns = ['Total Revenue', 'Order Count', 'Avg Order Value', 'Unique Customers', 'Returns']
age_analysis['Revenue per Customer'] = (age_analysis['Total Revenue'] / age_analysis['Unique Customers']).round(2)
age_analysis['Return Rate %'] = (age_analysis['Returns'] / age_analysis['Order Count'] * 100).round(2)
print(age_analysis)

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
df.groupby('age_group')['revenue'].sum().plot(kind='bar', ax=axes[0], color='darkblue')
axes[0].set_title('Revenue by Age Group')
axes[0].set_ylabel('Total Revenue ($)')
axes[0].set_xlabel('Age Group')

(df.groupby('age_group')['revenue'].sum() / df.groupby('age_group')['customer_id'].nunique()).plot(kind='bar', ax=axes[1], color='darkred')
axes[1].set_title('Revenue per Customer by Age Group')
axes[1].set_ylabel('Revenue per Customer ($)')
axes[1].set_xlabel('Age Group')
plt.tight_layout()
plt.savefig('dashboard/age_group_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 8. CATEGORY ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("8. PRODUCT CATEGORY ANALYSIS")
print("="*80)

category_analysis = df.groupby('category').agg({
    'revenue': ['sum', 'count', 'mean'],
    'gross_profit': 'sum',
    'returned': 'sum'
}).round(2)
category_analysis.columns = ['Total Revenue', 'Order Count', 'Avg Order Value', 'Gross Profit', 'Returns']
category_analysis['Return Rate %'] = (category_analysis['Returns'] / category_analysis['Order Count'] * 100).round(2)
category_analysis['Profit Margin %'] = (category_analysis['Gross Profit'] / category_analysis['Total Revenue'] * 100).round(2)
category_analysis = category_analysis.sort_values('Total Revenue', ascending=False)
print(category_analysis)

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
df.groupby('category')['revenue'].sum().sort_values(ascending=False).plot(kind='bar', ax=axes[0], color='mediumseagreen')
axes[0].set_title('Revenue by Product Category')
axes[0].set_ylabel('Total Revenue ($)')
axes[0].set_xlabel('Category')

return_by_category = (df.groupby('category')['returned'].sum() / df.groupby('category').size() * 100).sort_values(ascending=False)
return_by_category.plot(kind='bar', ax=axes[1], color='crimson')
axes[1].set_title('Return Rate by Product Category')
axes[1].set_ylabel('Return Rate (%)')
axes[1].set_xlabel('Category')
plt.tight_layout()
plt.savefig('dashboard/category_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 9. CUSTOMER RATING & RETURN CORRELATION
# ============================================================================
print("\n" + "="*80)
print("9. CUSTOMER RATING & RETURN CORRELATION")
print("="*80)

rating_return = df.groupby('customer_rating').agg({
    'returned': ['sum', 'count']
}).round(2)
rating_return.columns = ['Returns', 'Total Orders']
rating_return['Return Rate %'] = (rating_return['Returns'] / rating_return['Total Orders'] * 100).round(2)
print(rating_return)

# Visualization
fig, ax = plt.subplots(figsize=(10, 6))
return_by_rating = df.groupby('customer_rating')['returned'].sum() / df.groupby('customer_rating').size() * 100
return_by_rating.plot(kind='bar', ax=ax, color='navy')
ax.set_title('Return Rate by Customer Rating')
ax.set_ylabel('Return Rate (%)')
ax.set_xlabel('Customer Rating')
plt.tight_layout()
plt.savefig('dashboard/rating_return_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 10. SAVE SUMMARY TO SQLITE
# ============================================================================
print("\n" + "="*80)
print("10. SAVING ANALYSIS TO DATABASE")
print("="*80)

conn = sqlite3.connect('data/sales_analysis.sqlite')

# Save aggregated tables
top_products.to_sql('top_products_by_revenue', conn, if_exists='replace', index=True)
channel_performance.to_sql('channel_performance', conn, if_exists='replace', index=True)
region_analysis.to_sql('region_analysis', conn, if_exists='replace', index=True)
campaign_performance.to_sql('campaign_performance', conn, if_exists='replace', index=True)
age_analysis.to_sql('age_group_analysis', conn, if_exists='replace', index=True)
category_analysis.to_sql('category_analysis', conn, if_exists='replace', index=True)

conn.close()
print("✓ Analysis saved to: data/sales_analysis.sqlite")

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
print("\nAll visualizations saved to: dashboard/")
print("All datasets saved to: data/sales_analysis.sqlite")
print("\nKey Insights:")
print(f"  • Overall Return Rate: {return_rate:.2f}%")
print(f"  • Gross Profit Margin: {(df['gross_profit'].sum() / df['revenue'].sum() * 100):.2f}%")
print(f"  • Best Performing Channel: {channel_performance.index[0]} (${channel_performance.iloc[0]['Total Revenue']:,.2f})")
print(f"  • Highest Return Rate Region: {region_analysis['Return Rate %'].idxmax()}")
print(f"  • Top Product: {top_products.index[0]}")
