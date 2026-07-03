import sqlite3

def load_data(data):
    # Connect to SQLite database
    conn = sqlite3.connect("DB_NAME")

    # Create cursor object
    cursor = conn.cursor()

    # Create table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            order_id INTEGER,
            customer_name TEXT,
            product TEXT,
            quantity INTEGER,
            price REAL,
            total_amount REAL
        )
    """)

    # Insert data into the table
    for _, row in data.iterrows():
        cursor.execute(
            """
            INSERT INTO sales
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                row["order_id"],
                row["customer_name"],
                row["product"],
                row["quantity"],
                row["price"],
                row["total_amount"]
            )
        )

    # Save changes
    conn.commit()

    # Close connection
    cursor.close()
    conn.close()

    print("Data loaded successfully into sales.db")
