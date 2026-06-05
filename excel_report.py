import sqlite3
import pandas as pd

conn = sqlite3.connect("inventory.db")

products = pd.read_sql(
    "SELECT * FROM products",
    conn
)

orders = pd.read_sql(
    "SELECT * FROM orders",
    conn
)

suppliers = pd.read_sql(
    "SELECT * FROM suppliers",
    conn
)

supplier_kpi = orders.groupby(
    "supplier_id"
).agg({
    "quantity_ordered":"sum",
    "quantity_received":"sum"
})

supplier_kpi["Fill Rate %"] = (
    supplier_kpi["quantity_received"]
    /
    supplier_kpi["quantity_ordered"]
) * 100

with pd.ExcelWriter(
    "inventory_kpi_report.xlsx",
    engine="openpyxl"
) as writer:

    products.to_excel(
        writer,
        sheet_name="Inventory",
        index=False
    )

    suppliers.to_excel(
        writer,
        sheet_name="Suppliers",
        index=False
    )

    orders.to_excel(
        writer,
        sheet_name="Orders",
        index=False
    )

    supplier_kpi.to_excel(
        writer,
        sheet_name="Supplier KPI"
    )

print("Excel Report Generated")