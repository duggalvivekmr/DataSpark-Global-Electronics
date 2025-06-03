# 📊 SQL queries for business KPIs
sql_queries = [
    ("Total Revenue", """
SELECT ROUND(SUM(order_value), 2) AS total_revenue
FROM sales;
"""),
    ("Top 5 Products by Revenue", """
SELECT p.product_name, SUM(s.order_value) AS revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 5;
"""),
    ("Top 5 Products by Quantity Sold", """
SELECT p.product_name, SUM(s.quantity) AS total_units
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_units DESC
LIMIT 5;
"""),
    ("Top 5 Most Profitable Products", """
SELECT p.product_name,
       SUM((p.unit_price - p.unit_cost) * s.quantity) AS total_profit
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_profit DESC
LIMIT 5;
"""),
    ("Average Order Value Per Customer", """
SELECT c.customer_id,
       ROUND(AVG(s.order_value), 2) AS avg_order_value
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY avg_order_value DESC
LIMIT 10;
"""),
    ("Top 5 Customer States by Revenue", """
SELECT cu.state, ROUND(SUM(s.order_value), 2) AS total_revenue
FROM sales s
JOIN customers cu ON s.customer_id = cu.customer_id
GROUP BY cu.state
ORDER BY total_revenue DESC
LIMIT 5;
"""),
    ("Store-Level Performance: Revenue and Order Count", """
SELECT st.store_id,
       ROUND(SUM(s.order_value), 2) AS revenue,
       COUNT(s.order_id) AS order_count
FROM sales s
JOIN stores st ON s.store_id = st.store_id
GROUP BY st.store_id
ORDER BY revenue DESC;
"""),
    ("Monthly Sales Trend", """
SELECT DATE_TRUNC('month', order_date) AS month,
       ROUND(SUM(order_value), 2) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;
"""),
    ("Currency-Wise Sales Breakdown", """
SELECT currency_code, ROUND(SUM(order_value), 2) AS total_sales
FROM sales
GROUP BY currency_code
ORDER BY total_sales DESC;
"""),
    ("Revenue Normalized by Exchange Rate (USD Equivalent)", """
SELECT s.currency_code,
       ROUND(SUM(s.order_value / e.exchange_rate), 2) AS usd_equivalent_sales
FROM sales s
JOIN exchange_rates e ON s.order_date = e.date AND s.currency_code = e.currency
GROUP BY s.currency_code
ORDER BY usd_equivalent_sales DESC;
""")
]

