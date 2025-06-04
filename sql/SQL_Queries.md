
# 📊 SQL Queries Used in DataSpark: Global Electronics Project

---

## 🛠 Create Table in `global_electronics` Database

```sql
CREATE TABLE sales_full (
    `Order Number` INT,
    `Line Item` INT,
    `Order Date` DATETIME,
    `Delivery Date` DATETIME,
    `CustomerKey` INT,
    `StoreKey` INT,
    `ProductKey` INT,
    `Quantity` INT,
    `Currency Code` VARCHAR(10),
    `DeliveryMissing` VARCHAR(10),
    `Gender` VARCHAR(10),
    `Name` VARCHAR(255),
    `City` VARCHAR(100),
    `State Code` VARCHAR(50),
    `State_x` VARCHAR(100),
    `Zip Code` VARCHAR(20),
    `Country_x` VARCHAR(100),
    `Continent` VARCHAR(50),
    `Birthday` VARCHAR(50),
    `Product Name` VARCHAR(255),
    `Brand` VARCHAR(100),
    `Color` VARCHAR(50),
    `Unit Cost USD` DOUBLE,
    `Unit Price USD` DOUBLE,
    `SubcategoryKey` INT,
    `Subcategory` VARCHAR(100),
    `CategoryKey` INT,
    `Category` VARCHAR(100),
    `Country_y` VARCHAR(100),
    `State_y` VARCHAR(100),
    `Square Meters` DOUBLE,
    `Open Date` VARCHAR(50),
    `Exchange` DOUBLE
);
```

---

## 💰 Total Revenue

```sql
SELECT ROUND(SUM(`Unit Price USD` * Quantity), 2) AS Total_Revenue
FROM sales_full;
```

---

## 🛍️ Top 5 Selling Products by Revenue

```sql
SELECT 
    `Product Name`, 
    ROUND(SUM(`Unit Price USD` * Quantity), 2) AS Total_Revenue
FROM sales_full
GROUP BY `Product Name`
ORDER BY Total_Revenue DESC
LIMIT 5;
```

---

## 📦 Top 5 Products by Quantity Sold

```sql
SELECT 
    `Product Name`, 
    SUM(Quantity) AS Total_Quantity
FROM sales_full
GROUP BY `Product Name`
ORDER BY Total_Quantity DESC
LIMIT 5;
```

---

## 💹 Top 5 Most Profitable Products

```sql
SELECT 
    `Product Name`,
    ROUND(SUM((`Unit Price USD` - `Unit Cost USD`) * Quantity), 2) AS Total_Profit
FROM sales_full
GROUP BY `Product Name`
ORDER BY Total_Profit DESC
LIMIT 5;
```

---

## 📈 Average Order Value Per Customer

```sql
SELECT 
    CustomerKey,
    ROUND(SUM(`Unit Price USD` * Quantity) / COUNT(DISTINCT `Order Number`), 2) AS AvgOrderValue
FROM sales_full
GROUP BY CustomerKey
ORDER BY AvgOrderValue DESC;
```

---

## 🗺️ Top 5 Customer States by Revenue

```sql
SELECT 
    `State_x` AS CustomerState,
    ROUND(SUM(`Unit Price USD` * Quantity), 2) AS TotalRevenue
FROM sales_full
GROUP BY `State_x`
ORDER BY TotalRevenue DESC
LIMIT 5;
```

---

## 🏬 Store-Level Performance: Revenue and Order Count

```sql
SELECT 
    StoreKey,
    ROUND(SUM(`Unit Price USD` * Quantity), 2) AS Revenue
FROM sales_full
GROUP BY StoreKey
ORDER BY Revenue DESC;
```

---

## 📅 Monthly Sales Trend

```sql
SELECT 
    DATE_FORMAT(`Order Date`, '%Y-%m') AS Month,
    ROUND(SUM(`Unit Price USD` * Quantity), 2) AS Revenue
FROM sales_full
GROUP BY Month
ORDER BY Month;
```

---

## 🚻 Customer Gender Distribution

```sql
SELECT 
    Gender,
    COUNT(*) AS Customer_Count
FROM sales_full
GROUP BY Gender;
```

---

## 🎂 Customer Age Group Analysis

```sql
SELECT
    FLOOR(DATEDIFF(CURDATE(), STR_TO_DATE(Birthday, '%Y-%m-%d')) / 365) AS Age,
    COUNT(*) AS Customer_Count
FROM sales_full
WHERE Birthday IS NOT NULL
GROUP BY Age
ORDER BY Age;
```

---

## 🌍 Revenue Normalized by Exchange Rate (USD Equivalent)

```sql
SELECT 
    ROUND(SUM(`Unit Price USD` * Quantity * Exchange), 2) AS Revenue_USD_Equivalent
FROM sales_full;
```
