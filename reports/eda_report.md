# Exploratory Data Analysis Report

## Executive Summary
- Total records analyzed: 248
- Completed orders: 209
- Completed-order revenue: Rs. 7,813,182.32
- Average order value: Rs. 37,383.65
- Return rate: 10.5%
- Cancellation rate: 5.2%
- Top product by revenue: Laptop
- Top region by revenue: West

## Descriptive Statistics
| metric | quantity | unit_price | discount_rate | gross_revenue | net_revenue | customer_age |
| --- | --- | --- | --- | --- | --- | --- |
| count | 248.0 | 248.0 | 248.0 | 248.0 | 248.0 | 248.0 |
| mean | 1.96 | 18785.66 | 0.09 | 39584.04 | 35665.08 | 35.23 |
| std | 1.17 | 23888.67 | 0.08 | 65796.04 | 58211.85 | 8.99 |
| min | 1.0 | 492.19 | 0.0 | 492.19 | 458.46 | 20.0 |
| 25% | 1.0 | 2002.48 | 0.0 | 3081.57 | 2761.09 | 27.0 |
| 50% | 2.0 | 7087.94 | 0.1 | 12527.86 | 11294.96 | 35.5 |
| 75% | 3.0 | 23177.5 | 0.15 | 47461.34 | 45268.96 | 42.0 |
| max | 5.0 | 87361.97 | 0.2 | 344622.98 | 323938.32 | 50.0 |

## Categorical Profile
- Product Count: 6
- Region Count: 6
- Sales Channel Count: 3
- Customer Segment Count: 4
- Payment Mode Count: 5

## Monthly Revenue Trend
| order_month | revenue |
| --- | --- |
| 2025-01 | 435963.01 |
| 2025-02 | 243839.33000000002 |
| 2025-03 | 717323.18 |
| 2025-04 | 726580.65 |
| 2025-05 | 821404.74 |
| 2025-06 | 374965.61 |
| 2025-07 | 934348.16 |
| 2025-08 | 151693.85 |
| 2025-09 | 996051.15 |
| 2025-10 | 472066.92 |

## Top Products by Revenue
| product | revenue | orders | units |
| --- | --- | --- | --- |
| Laptop | 4673353.01 | 33 | 76 |
| Smartphone | 1594178.82 | 33 | 71 |
| Monitor | 1159674.01 | 41 | 80 |
| Headphones | 183659.66 | 37 | 80 |
| Keyboard | 121700.33 | 34 | 57 |
| Mouse | 80616.49 | 31 | 56 |

## Revenue by Region
| region | revenue | orders |
| --- | --- | --- |
| West | 2014049.59 | 46 |
| North | 1458974.6 | 42 |
| East | 1456594.55 | 41 |
| Central | 1439239.55 | 35 |
| South | 1294837.3900000001 | 42 |
| Unknown | 149486.64 | 3 |

## Revenue by Sales Channel
| sales_channel | revenue | orders |
| --- | --- | --- |
| Retail | 2808826.05 | 73 |
| Online | 2804653.91 | 70 |
| Partner | 2199702.36 | 66 |

## Revenue by Customer Segment
| customer_segment | revenue | avg_order_value | orders |
| --- | --- | --- | --- |
| Small Business | 2445247.69 | 45282.36462962963 | 54 |
| Student | 1907198.42 | 33459.62140350877 | 57 |
| Enterprise | 1762736.49 | 36723.676875 | 48 |
| Professional | 1697999.72 | 33959.994399999996 | 50 |

## Correlation Matrix
| field | quantity | unit_price | discount_rate | customer_age | net_revenue |
| --- | --- | --- | --- | --- | --- |
| quantity | 1.0 | 0.099 | 0.118 | -0.06 | 0.497 |
| unit_price | 0.099 | 1.0 | 0.009 | 0.046 | 0.783 |
| discount_rate | 0.118 | 0.009 | 1.0 | -0.026 | 0.035 |
| customer_age | -0.06 | 0.046 | -0.026 | 1.0 | 0.034 |
| net_revenue | 0.497 | 0.783 | 0.035 | 0.034 | 1.0 |

## Key Insights
- Laptop generated the highest completed-order revenue.
- West was the strongest region by revenue.
- Sales performance should be monitored monthly because revenue varies by order month.
- Product, region, channel, and segment cuts provide useful dashboard dimensions for business users.
- Return and cancellation rates should be tracked because they reduce realized sales impact.

## Recommended KPIs for Dashboard
- Completed-order revenue
- Average order value
- Completed orders
- Return rate
- Cancellation rate
- Revenue by month, product, region, channel, and customer segment
