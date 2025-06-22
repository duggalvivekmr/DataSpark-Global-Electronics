import pandas as pd

# Load your cleaned CSV
csv_file_path = r"D:\Education\Data Science\Project\DataSpark Illuminating Insights for Global Electronics\DataSpark-Global-Electronics\data\clean\sales_full_cleaned.csv"
df = pd.read_csv(csv_file_path)

# Replace empty strings with NaT in the 'Delivery Date' column
df['Delivery Date'] = df['Delivery Date'].replace('', pd.NaT)
df['Order Date'] = df['Order Date'].replace('', pd.NaT)
df['Open Date'] = df['Open Date'].replace('', pd.NaT)

# Save to a new file
fixed_file_path = r"D:\Education\Data Science\Project\DataSpark Illuminating Insights for Global Electronics\DataSpark-Global-Electronics\data\clean\sales_full_cleaned_fixed.csv"
df.to_csv(fixed_file_path, index=False)

print("✅ Cleaned CSV saved to:")
print(fixed_file_path)

