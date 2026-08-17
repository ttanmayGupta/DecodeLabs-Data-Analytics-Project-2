import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load dataset
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

print("=" * 60)
print("DECODELABS - PROJECT 2: EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# 2. Basic information
print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATASET SHAPE:")
print(df.shape)

print("\nDATA TYPES:")
print(df.dtypes)

print("\nMISSING VALUES:")
print(df.isnull().sum())

# 3. Basic statistics: count, mean, median
numeric_cols = ["Quantity", "Sales", "Profit"]
print("\nBASIC STATISTICS:")
print(df[numeric_cols].agg(["count", "mean", "median"]).round(2))

# 4. Trend analysis
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMONTHLY SALES:")
print(monthly_sales.round(2))

print("\nHIGHEST SALES MONTH:")
print(monthly_sales.idxmax(), "=", round(monthly_sales.max(), 2))

print("\nLOWEST SALES MONTH:")
print(monthly_sales.idxmin(), "=", round(monthly_sales.min(), 2))

# 5. Outlier detection using IQR
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Sales"] < lower_bound) | (df["Sales"] > upper_bound)]

print("\nOUTLIER LIMITS:")
print("Lower bound:", round(lower_bound, 2))
print("Upper bound:", round(upper_bound, 2))

print("\nOUTLIERS:")
print(outliers[["Date", "Product", "Sales", "Profit"]])

# 6. Category analysis
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nSALES BY CATEGORY:")
print(category_sales.round(2))

# 7. Create graphs folder
os.makedirs("graphs", exist_ok=True)

# Graph 1: Monthly Sales Trend
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/monthly_sales_trend.png", dpi=150)
plt.close()

# Graph 2: Category Sales
plt.figure(figsize=(7, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("graphs/category_sales.png", dpi=150)
plt.close()

# Graph 3: Quantity vs Sales
plt.figure(figsize=(7, 5))
plt.scatter(df["Quantity"], df["Sales"])
plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("graphs/quantity_vs_sales.png", dpi=150)
plt.close()

print("\n3 graphs saved inside the 'graphs' folder.")
print("\nEDA PROJECT COMPLETED SUCCESSFULLY!")
