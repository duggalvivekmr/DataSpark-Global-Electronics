import pandas as pd
import sqlite3
import os

# Define paths to cleaned data
data_path = "data/clean"
csv_files = {
    "sales": os.path.join(data_path, "sales_full.csv"),
    "sales_delivered": os.path.join(data_path, "sales_delivered.csv"),
    "sales_undelivered": os.path.join(data_path, "sales_undelivered.csv"),
}

# Add raw datasets for joins
raw_path = "data/raw"
csv_files.update({
    "customers": os.path.join(raw_path, "Customers.csv"),
    "products": os.path.join(raw_path, "Products.csv"),
    "stores": os.path.join(raw_path, "Stores.csv"),
    "exchange_rates": os.path.join(raw_path, "Exchange_Rates.csv"),
})

# Create and Connect to SQLite database
conn = sqlite3.connect("sql/global_electronics.db")

# Load each CSV into a table
for table_name, file_path in csv_files.items():
    try:
        # Use special encoding only for 'customers' table
        if table_name == "customers":
            df = pd.read_csv(file_path, encoding='ISO-8859-1')
        else:    
            df = pd.read_csv(file_path)
        
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"✅ Loaded {table_name} into database.")
    except Exception as e:
        print(f"⚠️ Failed to load {table_name}: {e}")
conn.close()
print("🎉 Database created: global_electronics.db")