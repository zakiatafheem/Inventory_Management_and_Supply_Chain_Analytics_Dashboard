import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

products = [
    ("Steel Rod", "Raw Material", "Warehouse A", 450, 100),
    ("Copper Wire", "Raw Material", "Warehouse B", 250, 80),
    ("Aluminum Sheet", "Raw Material", "Warehouse A", 600, 120),
    ("Plastic Parts", "Components", "Warehouse C", 150, 50),
    ("Electronic Board", "Components", "Warehouse B", 90, 40)
]

cursor.executemany("""
INSERT INTO products
(product_name, category, warehouse, stock_quantity, reorder_level)
VALUES (?, ?, ?, ?, ?)
""", products)

suppliers = [
    ("ABC Suppliers", 7, 95),
    ("Global Traders", 10, 88),
    ("Prime Materials", 5, 98),
    ("Supply Hub", 12, 80)
]

cursor.executemany("""
INSERT INTO suppliers
(supplier_name, lead_time_days, reliability_score)
VALUES (?, ?, ?)
""", suppliers)

for i in range(100):

    product_id = random.randint(1, 5)
    supplier_id = random.randint(1, 4)

    qty_ordered = random.randint(50, 500)

    qty_received = qty_ordered - random.randint(0, 20)

    order_date = datetime.now() - timedelta(days=random.randint(1, 180))

    delivery_date = order_date + timedelta(days=random.randint(4, 15))

    cursor.execute("""
    INSERT INTO orders
    (product_id, supplier_id,
     quantity_ordered, quantity_received,
     order_date, delivery_date)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        product_id,
        supplier_id,
        qty_ordered,
        qty_received,
        order_date.strftime("%Y-%m-%d"),
        delivery_date.strftime("%Y-%m-%d")
    ))

conn.commit()
conn.close()

print("Sample Data Inserted")