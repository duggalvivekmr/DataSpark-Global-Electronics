import pandas as pd
import mysql.connector
from mysql.connector import Error
import os

# Load cleaned CSV
csv_file_path = r"C:\Users\VivekKumarDuggal\Desktop\DataSpark-Project\DataSpark-Global-Electronics\data\clean\sales_full_cleaned.csv"
df = pd.read_csv(csv_file_path)

# Replace NaN with None for SQL compatibility
df = df.where(pd.notnull(df), None)

# Fill in your MySQL credentials
mysql_config = {
    'host': 'host',           # Replace with your host
    'user': 'username',                # Replace with your MySQL username
    'password': 'your_password',    # Replace with your MySQL password
    'database': 'global_electronics'  # Replace with your database name
}

# Connect to MySQL and insert data
try:
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()

    # Prepare INSERT SQL
    columns = ", ".join([f"`{col}`" for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))
    insert_query = f"INSERT INTO sales_full ({columns}) VALUES ({placeholders})"

    # Convert DataFrame to list of tuples
    data = [tuple(row) for row in df.itertuples(index=False, name=None)]

    # Execute batch insert
    cursor.executemany(insert_query, data)
    connection.commit()

    print(f"{cursor.rowcount} rows inserted successfully.")

except Error as e:
    print("Error:", e)

finally:
    try:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
    except:
        pass