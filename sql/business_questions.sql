-- top_5_products_by_revenue
SELECT product, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS completed_orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY product
ORDER BY revenue DESC
LIMIT 5;

-- monthly_revenue_trend
SELECT order_month, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS completed_orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY order_month
ORDER BY order_month;

-- revenue_by_region
SELECT region, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS completed_orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY region
ORDER BY revenue DESC;

-- sales_channel_performance
SELECT sales_channel, ROUND(SUM(net_revenue), 2) AS revenue, ROUND(AVG(net_revenue), 2) AS avg_order_value
FROM sales
WHERE order_status = 'Completed'
GROUP BY sales_channel
ORDER BY revenue DESC;

-- customer_segment_performance
SELECT customer_segment, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(DISTINCT customer_id) AS customers
FROM sales
WHERE order_status = 'Completed'
GROUP BY customer_segment
ORDER BY revenue DESC;

-- return_and_cancellation_by_product
SELECT product,
       ROUND(AVG(CASE WHEN order_status = 'Returned' THEN 1.0 ELSE 0 END) * 100, 2) AS return_rate_pct,
       ROUND(AVG(CASE WHEN order_status = 'Cancelled' THEN 1.0 ELSE 0 END) * 100, 2) AS cancellation_rate_pct
FROM sales
GROUP BY product
ORDER BY return_rate_pct DESC, cancellation_rate_pct DESC;

-- payment_mode_revenue
SELECT payment_mode, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY payment_mode
ORDER BY revenue DESC;
