# Inventory Management & Supply Chain Analytics Dashboard

## Project Overview

The Inventory Management & Supply Chain Analytics Dashboard is a data analytics project designed to help organizations monitor inventory levels, track stock movement, evaluate supplier performance, and improve supply chain efficiency.

The project integrates Python, SQL, Excel, and Power BI to automate data processing, generate key performance indicators (KPIs), and visualize business insights through an interactive dashboard.

---

# Problem Statement

Organizations often face challenges such as:

- Excess inventory leading to higher carrying costs
- Stock shortages affecting customer fulfillment
- Inefficient supplier performance monitoring
- Manual reporting processes consuming significant time
- Lack of visibility into inventory and supply chain operations

This project aims to address these challenges by creating a centralized analytics solution for inventory and supply chain management.

---

# Objectives

- Monitor inventory levels across warehouses
- Identify low-stock products and stock-out risks
- Track supplier reliability and delivery performance
- Analyze lead times and procurement efficiency
- Automate reporting and KPI generation
- Support data-driven inventory optimization decisions

---

# Features

### Inventory Analytics

- Inventory tracking across warehouses
- Stock quantity monitoring
- Low stock identification
- Reorder level analysis

### Supplier Analytics

- Supplier reliability tracking
- Fill rate analysis
- Lead time monitoring
- Supplier performance comparison

### Reporting & Automation

- Automated data extraction using SQL
- Data cleaning and processing using Python
- Excel KPI report generation
- Interactive Power BI dashboard

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Data Processing & Analytics |
| Pandas | Data Manipulation |
| NumPy | Numerical Calculations |
| SQLite | Database Management |
| SQL | Data Extraction |
| Excel | KPI Reporting |
| Power BI | Dashboard Visualization |

---

# Project Architecture

```text
Inventory Database
       |
       v
SQL Queries
       |
       v
Python Data Processing
(Pandas + NumPy)
       |
       +----------------+
       |                |
       v                v
Excel Reports      Power BI Dashboard
```

---

# Database Schema

## Products Table

| Column |
|---------|
| product_id |
| product_name |
| category |
| warehouse |
| stock_quantity |
| reorder_level |

## Suppliers Table

| Column |
|---------|
| supplier_id |
| supplier_name |
| lead_time_days |
| reliability_score |

## Orders Table

| Column |
|---------|
| order_id |
| product_id |
| supplier_id |
| quantity_ordered |
| quantity_received |
| order_date |
| delivery_date |

---
# Project Outcomes

- Automated inventory monitoring process.
- Reduced manual reporting effort.
- Improved visibility into supplier performance.
- Enabled proactive stock replenishment planning.
- Supported data-driven procurement decisions.

---

# Challenges Faced

- Designing realistic inventory datasets.
- Managing data consistency across multiple tables.
- Calculating supplier performance metrics.
- Building meaningful KPIs for supply chain analysis.
- Creating user-friendly dashboard visualizations.

---
