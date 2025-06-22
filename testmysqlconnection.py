from mysql.connector import connect, Error

try:
    conn = connect(
        host="localhost",
        user="root",
        password="your_password",  # Replace with your real password
        database="global_electronics"
    )
    print("Connection successful!")
except Error as e:
    print("Error:", e)
