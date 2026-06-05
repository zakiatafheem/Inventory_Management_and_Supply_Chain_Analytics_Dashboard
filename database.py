import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Product Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    warehouse TEXT,
    stock_quantity INTEGER,
    reorder_level INTEGER
)
""")

# Supplier Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name TEXT,
    lead_time_days INTEGER,
    reliability_score REAL
)
""")

# Orders Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    supplier_id INTEGER,
    quantity_ordered INTEGER,
    quantity_received INTEGER,
    order_date TEXT,
    delivery_date TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")