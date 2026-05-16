# SQL Query Results

## Top 5 Products By Revenue

```sql
SELECT product, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS completed_orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY product
ORDER BY revenue DESC
LIMIT 5;
```

| product | revenue | completed_orders |
| --- | --- | --- |
| Laptop | 4673353.01 | 33 |
| Smartphone | 1594178.82 | 33 |
| Monitor | 1159674.01 | 41 |
| Headphones | 183659.66 | 37 |
| Keyboard | 121700.33 | 34 |

## Monthly Revenue Trend

```sql
SELECT order_month, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS completed_orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY order_month
ORDER BY order_month;
```

| order_month | revenue | completed_orders |
| --- | --- | --- |
| 2025-01 | 435963.01 | 19 |
| 2025-02 | 243839.33 | 8 |
| 2025-03 | 717323.18 | 24 |
| 2025-04 | 726580.65 | 15 |
| 2025-05 | 821404.74 | 23 |
| 2025-06 | 374965.61 | 12 |
| 2025-07 | 934348.16 | 20 |
| 2025-08 | 151693.85 | 13 |
| 2025-09 | 996051.15 | 16 |
| 2025-10 | 472066.92 | 15 |
| 2025-11 | 1411316.3 | 20 |
| 2025-12 | 527629.42 | 24 |

## Revenue By Region

```sql
SELECT region, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS completed_orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY region
ORDER BY revenue DESC;
```

| region | revenue | completed_orders |
| --- | --- | --- |
| West | 2014049.59 | 46 |
| North | 1458974.6 | 42 |
| East | 1456594.55 | 41 |
| Central | 1439239.55 | 35 |
| South | 1294837.39 | 42 |
| Unknown | 149486.64 | 3 |

## Sales Channel Performance

```sql
SELECT sales_channel, ROUND(SUM(net_revenue), 2) AS revenue, ROUND(AVG(net_revenue), 2) AS avg_order_value
FROM sales
WHERE order_status = 'Completed'
GROUP BY sales_channel
ORDER BY revenue DESC;
```

| sales_channel | revenue | avg_order_value |
| --- | --- | --- |
| Retail | 2808826.05 | 38477.07 |
| Online | 2804653.91 | 40066.48 |
| Partner | 2199702.36 | 33328.82 |

## Customer Segment Performance

```sql
SELECT customer_segment, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(DISTINCT customer_id) AS customers
FROM sales
WHERE order_status = 'Completed'
GROUP BY customer_segment
ORDER BY revenue DESC;
```

| customer_segment | revenue | customers |
| --- | --- | --- |
| Small Business | 2445247.69 | 44 |
| Student | 1907198.42 | 46 |
| Enterprise | 1762736.49 | 40 |
| Professional | 1697999.72 | 39 |

## Return And Cancellation By Product

```sql
SELECT product,
       ROUND(AVG(CASE WHEN order_status = 'Returned' THEN 1.0 ELSE 0 END) * 100, 2) AS return_rate_pct,
       ROUND(AVG(CASE WHEN order_status = 'Cancelled' THEN 1.0 ELSE 0 END) * 100, 2) AS cancellation_rate_pct
FROM sales
GROUP BY product
ORDER BY return_rate_pct DESC, cancellation_rate_pct DESC;
```

| product | return_rate_pct | cancellation_rate_pct |
| --- | --- | --- |
| Smartphone | 18.18 | 6.82 |
| Mouse | 13.16 | 5.26 |
| Monitor | 8.89 | 0.0 |
| Headphones | 8.7 | 10.87 |
| Keyboard | 7.69 | 5.13 |
| Laptop | 5.56 | 2.78 |

## Payment Mode Revenue

```sql
SELECT payment_mode, ROUND(SUM(net_revenue), 2) AS revenue, COUNT(*) AS orders
FROM sales
WHERE order_status = 'Completed'
GROUP BY payment_mode
ORDER BY revenue DESC;
```

| payment_mode | revenue | orders |
| --- | --- | --- |
| Upi | 2760937.75 | 38 |
| Credit Card | 1561455.58 | 44 |
| Net Banking | 1245129.34 | 42 |
| Cash | 1167390.35 | 44 |
| Debit Card | 1078269.3 | 41 |
