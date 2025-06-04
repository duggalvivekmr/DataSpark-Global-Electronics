USE global_electronics;
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

# 1---CALCULATE TOTAL REVENUE---
SELECT ROUND(SUM(`Unit Price USD` * Quantity), 2) AS Total_Revenue
FROM sales_full;

# 2---TOP 5 SELLING PRODUCTS BY REVENUE---
SELECT 
    `Product Name`, 
    ROUND(SUM(`Unit Price USD` * Quantity), 2) AS Total_Revenue
FROM sales_full
GROUP BY `Product Name`
ORDER BY Total_Revenue DESC
LIMIT 5;

# 3---TOP 5 PRODUCTS BY QUANTITY SOLD---
SELECT 
    `Product Name`, 
    SUM(Quantity) AS Total_Quantity
FROM sales_full
GROUP BY `Product Name`
ORDER BY Total_Quantity DESC
LIMIT 5;

# 4---TOP 5 PRODUCT PROFITABILITY---
SELECT 
    `Product Name`,
    ROUND(SUM((`Unit Price USD` - `Unit Cost USD`) * Quantity), 2) AS Total_Profit
FROM sales_full
GROUP BY `Product Name`
ORDER BY Total_Profit DESC
LIMIT 5;

# 5---REVENUE BY COUNTRY---
SELECT 
    Country_y AS Country,
    ROUND(SUM(`Unit Price USD` * Quantity), 2) AS Revenue
FROM sales_full
GROUP BY Country
ORDER BY Revenue DESC;

# 6---REVENUE NORMALIZED BY EXCHANGE RATE---
SELECT 
    ROUND(SUM(`Unit Price USD` * Quantity * Exchange), 2) AS Revenue_USD_Equivalent
FROM sales_full;

# 7---AVG ORDER VALUE PER CUSTOMER---
SELECT 
    CustomerKey,
    ROUND(SUM(`Unit Price USD` * Quantity) / COUNT(DISTINCT `Order Number`), 2) AS AvgOrderValue
FROM sales_full
GROUP BY CustomerKey
ORDER BY AvgOrderValue DESC;

# 8---STORE LEVEL PERFORMANCE BY REVENUE---
SELECT 
    StoreKey,
    ROUND(SUM(`Unit Price USD` * Quantity), 2) AS Revenue
FROM sales_full
GROUP BY StoreKey
ORDER BY Revenue DESC;

# 9---MONTHLY SALES TREND---
SELECT 
    DATE_FORMAT(`Order Date`, '%Y-%m') AS Month,
    ROUND(SUM(`Unit Price USD` * Quantity), 2) AS Revenue
FROM sales_full
GROUP BY Month
ORDER BY Month;

# 10---CUSTOMER GENDER DISTRIBUTION
SELECT 
    Gender, COUNT(*) AS Customer_Count
FROM sales_full
GROUP BY Gender;

# 11---CUSTOMER AGE GROUP ANALYSIS---
SELECT
	FLOOR(DATEDIFF(CURDATE(), STR_TO_DATE(Birthday, '%Y-%m-%d')) / 365) As Age,
    COUNT(*) AS Customer_Count
FROM sales_full
WHERE Birthday IS NOT NULL
GROUP BY Age
ORDER BY Age;

# 12---TOP 5 STATES BY CUSTOMER REVENUE----
SELECT 
    `State_x` AS CustomerState,
    ROUND(SUM(`Unit Price USD` * Quantity), 2) AS TotalRevenue
FROM sales_full
GROUP BY `State_x`
ORDER BY TotalRevenue DESC
LIMIT 5;


