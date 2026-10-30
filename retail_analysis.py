from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Locate the dataset
PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR /"data" / "Sample - Superstore.csv"

# Load the data
df = pd.read_csv(DATA_PATH, encoding="cp1252")

# Inspect the dataset
print("Dataset loaded successfully!")
print("Rows and columns:", df.shape)
print("\nFirst five rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())

# Basic dataset information
print("\n--- Dataset Information ---")
df.info()

# Statistical summary
print("\n--- Statistical Summary ---")
print(df.describe())

# Check missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Check duplicate rows
print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())


# ==============================
# DATA CLEANING
# ==============================

# Create a working copy of the original dataset
df_clean = df.copy()

# Convert date columns to datetime
df_clean["Order Date"] = pd.to_datetime(
    df_clean["Order Date"], errors="coerce"
)

df_clean["Ship Date"] = pd.to_datetime(
    df_clean["Ship Date"], errors="coerce"
)

# Treat Postal Code as an identifier
df_clean["Postal Code"] = (
    df_clean["Postal Code"].astype("string")
)

# Check whether date conversion introduced missing values
print("\n--- Date Conversion Check ---")
print("Invalid Order Dates:", df_clean["Order Date"].isna().sum())
print("Invalid Ship Dates:", df_clean["Ship Date"].isna().sum())

# Verify the updated data types
print("\n--- Updated Data Types ---")
print(df_clean.dtypes)

# Validate the data
print("\n--- Data Validation ---")
print("Rows and columns:", df_clean.shape)
print("Missing values:", df_clean.isnull().sum().sum())
print("Exact duplicate rows:", df_clean.duplicated().sum())


# ==============================
# EXPLORATORY DATA ANALYSIS
# ==============================

# 1. Calculate key business metrics
total_sales = df_clean["Sales"].sum()
total_profit = df_clean["Profit"].sum()
total_orders = df_clean["Order ID"].nunique()
total_customers = df_clean["Customer ID"].nunique()
total_quantity = df_clean["Quantity"].sum()

average_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100

print("\n--- KEY BUSINESS METRICS ---")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Total Items Sold: {total_quantity:,}")
print(f"Average Sales per Order: ${average_order_value:,.2f}")
print(f"Overall Profit Margin: {profit_margin:.2f}%")



# ==============================
# SALES AND PROFIT BY CATEGORY
# ==============================

category_analysis = df_clean.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Units_Sold=("Quantity", "sum")
).reset_index()

category_analysis["Profit_Margin_%"] = (
    category_analysis["Total_Profit"]
    / category_analysis["Total_Sales"] * 100
)

category_analysis = category_analysis.sort_values(
    by="Total_Sales", ascending=False
)

print("\n--- SALES AND PROFIT BY CATEGORY ---")
print(category_analysis.round(2).to_string(index=False))


# ==============================
# PERFORMANCE BY SUB-CATEGORY
# ==============================

subcategory_analysis = df_clean.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Units_Sold=("Quantity", "sum")
).reset_index()

subcategory_analysis = subcategory_analysis.sort_values(
    by="Total_Profit", ascending=False
)

print("\n--- TOP 5 SUB-CATEGORIES BY PROFIT ---")
print(subcategory_analysis.head(5).round(2).to_string(index=False))

print("\n--- BOTTOM 5 SUB-CATEGORIES BY PROFIT ---")
print(subcategory_analysis.tail(5).round(2).to_string(index=False))


# ==============================
# PERFORMANCE BY REGION
# ==============================

region_analysis = df_clean.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique")
).reset_index()

region_analysis = region_analysis.sort_values(
    by="Total_Profit", ascending=False
)

print("\n--- SALES AND PROFIT BY REGION ---")
print(region_analysis.round(2).to_string(index=False))

# ==============================
# VISUALIZATION: PROFIT BY CATEGORY
# ==============================

plt.figure(figsize=(9, 5))

sns.barplot(
    data=category_analysis,
    x="Category",
    y="Total_Profit"
)

plt.title("Total Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit ($)")
plt.tight_layout()
plt.savefig("profit_by_category.png", dpi=300)
plt.show()
