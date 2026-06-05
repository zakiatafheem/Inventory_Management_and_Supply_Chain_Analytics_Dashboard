import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect("inventory.db")

products = pd.read_sql("""
SELECT * FROM products
""", conn)

orders = pd.read_sql("""
SELECT * FROM orders
""", conn)

suppliers = pd.read_sql("""
SELECT * FROM suppliers
""", conn)

# Inventory Turnover

orders["inventory_turnover"] = (
    orders["quantity_received"] /
    orders["quantity_ordered"]
)

# Supplier Fill Rate

supplier_perf = orders.groupby("supplier_id").agg({
    "quantity_ordered":"sum",
    "quantity_received":"sum"
}).reset_index()

supplier_perf["fill_rate"] = (
    supplier_perf["quantity_received"] /
    supplier_perf["quantity_ordered"]
) * 100

# Stock Out Risk

products["stock_out_risk"] = np.where(
    products["stock_quantity"] <= products["reorder_level"],
    "High",
    "Low"
)

# Lead Time Analysis

orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["delivery_date"] = pd.to_datetime(orders["delivery_date"])

orders["lead_time"] = (
    orders["delivery_date"] -
    orders["order_date"]
).dt.days

lead_time_avg = (
    orders.groupby("supplier_id")["lead_time"]
    .mean()
    .reset_index()
)

print("\nStock Risk")
print(products[[
    "product_name",
    "stock_quantity",
    "reorder_level",
    "stock_out_risk"
]])

print("\nSupplier Performance")
print(supplier_perf)

print("\nAverage Lead Time")
print(lead_time_avg)

conn.close()