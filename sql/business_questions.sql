-- Task 2 Business Intelligence Queries
-- Using actual columns from the sales_transactions_cleaned.csv dataset

-- 1. What are the top products by revenue?
SELECT 
    product_name,
    ROUND(SUM(revenue), 2) as total_revenue,
    COUNT(*) as order_count,
    ROUND(AVG(revenue), 2) as avg_order_value,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END), 0) as return_count,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as return_rate_pct
FROM sales_data
GROUP BY product_name
ORDER BY total_revenue DESC;

-- 2. How is revenue trending month by month?
SELECT 
    strftime('%Y-%m', order_date) as year_month,
    ROUND(SUM(revenue), 2) as monthly_revenue,
    COUNT(*) as order_count,
    ROUND(AVG(revenue), 2) as avg_order_value,
    ROUND(SUM(revenue - cost), 2) as gross_profit
FROM sales_data
GROUP BY strftime('%Y-%m', order_date)
ORDER BY year_month;

-- 3. Which sales channel performs best?
SELECT 
    sales_channel,
    ROUND(SUM(revenue), 2) as total_revenue,
    COUNT(*) as order_count,
    ROUND(AVG(revenue), 2) as avg_order_value,
    ROUND(SUM(revenue - cost), 2) as gross_profit,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as return_rate_pct
FROM sales_data
GROUP BY sales_channel
ORDER BY total_revenue DESC;

-- 4. Which region has the highest return rate and lowest return rate?
SELECT 
    region,
    ROUND(SUM(revenue), 2) as total_revenue,
    COUNT(*) as order_count,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END), 0) as return_count,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as return_rate_pct
FROM sales_data
GROUP BY region
ORDER BY return_rate_pct DESC;

-- 5. Which campaign creates the strongest gross profit?
SELECT 
    campaign,
    ROUND(SUM(revenue), 2) as total_revenue,
    COUNT(*) as order_count,
    ROUND(SUM(revenue - cost), 2) as gross_profit,
    ROUND(SUM(revenue - cost) * 100.0 / SUM(revenue), 2) as profit_margin_pct,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as return_rate_pct
FROM sales_data
GROUP BY campaign
ORDER BY gross_profit DESC;

-- 6. Which customer age group has the highest revenue per customer?
SELECT 
    age_group,
    COUNT(DISTINCT customer_id) as unique_customers,
    COUNT(*) as order_count,
    ROUND(SUM(revenue), 2) as total_revenue,
    ROUND(SUM(revenue) / COUNT(DISTINCT customer_id), 2) as revenue_per_customer,
    ROUND(AVG(revenue), 2) as avg_order_value,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as return_rate_pct
FROM sales_data
GROUP BY age_group
ORDER BY revenue_per_customer DESC;

-- 7. Product Category Performance
SELECT 
    category,
    ROUND(SUM(revenue), 2) as total_revenue,
    COUNT(*) as order_count,
    ROUND(AVG(revenue), 2) as avg_order_value,
    ROUND(SUM(revenue - cost), 2) as gross_profit,
    ROUND(SUM(revenue - cost) * 100.0 / SUM(revenue), 2) as profit_margin_pct,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as return_rate_pct
FROM sales_data
GROUP BY category
ORDER BY total_revenue DESC;

-- 8. Payment Method Analysis
SELECT 
    payment_method,
    ROUND(SUM(revenue), 2) as total_revenue,
    COUNT(*) as order_count,
    ROUND(AVG(revenue), 2) as avg_order_value,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as return_rate_pct
FROM sales_data
GROUP BY payment_method
ORDER BY total_revenue DESC;

-- 9. Customer Rating Impact on Returns
SELECT 
    customer_rating,
    COUNT(*) as order_count,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END), 0) as return_count,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as return_rate_pct,
    ROUND(AVG(revenue), 2) as avg_order_value
FROM sales_data
GROUP BY customer_rating
ORDER BY customer_rating DESC;

-- 10. Sales Channel by Region - Performance Matrix
SELECT 
    region,
    sales_channel,
    ROUND(SUM(revenue), 2) as total_revenue,
    COUNT(*) as order_count,
    ROUND(AVG(revenue), 2) as avg_order_value,
    ROUND(SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as return_rate_pct
FROM sales_data
GROUP BY region, sales_channel
ORDER BY total_revenue DESC;
