import pandas as pd
import mysql.connector
from mysql.connector import Error

# === CONFIGURATION ===
csv_file_path = r"D:\Education\Data Science\Project\DataSpark Illuminating Insights for Global Electronics\DataSpark-Global-Electronics\data\clean\sales_full_cleaned_fixed.csv"

mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',  # Replace with your actual password
    'database': 'global_electronics'
}

# === LOAD CSV ===
try:
    df = pd.read_csv(csv_file_path)
    df = df.where(pd.notnull(df), None)  # Replace NaN with None for MySQL
    print("CSV Loaded Successfully")
    print("DataFrame shape:", df.shape)
    print("Sample rows:\n", df.head())
except Exception as e:
    print("Error loading CSV:", e)
    exit()

# === CONNECT TO MYSQL ===
try:
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    print("Connected to MySQL")
except Error as err:
    print("❌ MySQL connection failed!")
    print("Error details:", err)
    exit(1)

    # === COLUMN MATCH CHECK ===
    cursor.execute("DESCRIBE sales_full")
    db_cols = [col[0] for col in cursor.fetchall()]
    csv_cols = list(df.columns)

    print("\nColumns in MySQL table:")
    print(db_cols)
    print("\nColumns in CSV:")
    print(csv_cols)

    if db_cols != csv_cols:
        print("Column mismatch detected!")
    else:
        print("Column names match")

    # === PREPARE INSERT ===
    columns = ", ".join([f"`{col}`" for col in csv_cols])
    placeholders = ", ".join(["%s"] * len(csv_cols))
    insert_query = f"INSERT INTO sales_full ({columns}) VALUES ({placeholders})"
    print("\nGenerated INSERT query:\n", insert_query)

    # === PREPARE DATA ===
    data = [tuple(row) for row in df.itertuples(index=False, name=None)]

    # === TEST INSERT FIRST 5 ROWS ===
    print("\n Testing insertion of first 5 rows...")
    for i, row in enumerate(data[:5]):
        try:
            cursor.execute(insert_query, row)
            print(f" Row {i+1} inserted successfully.")
        except Error as err:
            print(f" Error inserting row {i+1}:", err)
            print(" Row content:", row)
            connection.rollback()
            break

    # === FINAL BATCH INSERT (optional: enable if test passes) ===
    try:    
        print("\n Inserting all data...")
        cursor.executemany(insert_query, data)
        connection.commit()
        print(f" {cursor.rowcount} rows inserted successfully.")

    except Error as err:
        print("Batch insert error:", err)
        connection.rollback()

except Error as err:
    print("❌ MySQL Connection Error:", err)

finally:
    try:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print(" MySQL connection closed.")
    except:
        pass
