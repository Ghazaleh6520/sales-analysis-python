import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
orders = pd.read_csv("C:/Users/ghazaleh.eidivandi/OneDrive - Interpublic/Desktop/sales-analysis-python/orders.csv")

# Create revenue column
orders["Revenue"] = orders["Quantity"] * orders["UnitPrice"]

# Preview data
print("=== First 5 rows ===")
print(orders.head())
print()

# Total revenue
total_revenue = orders["Revenue"].sum()
print(f"Total revenue: {total_revenue:.2f}")
print()

# Revenue by country
revenue_by_country = orders.groupby("ShipCountry")["Revenue"].sum().sort_values(ascending=False)
print("=== Revenue by country ===")
print(revenue_by_country)
print()

# Freight by country
freight_by_country = orders.groupby("ShipCountry")["Freight"].sum().sort_values(ascending=False)
print("=== Freight by country ===")
print(freight_by_country)
print()

# Revenue by category
revenue_by_category = orders.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
print("=== Revenue by category ===")
print(revenue_by_category)
print()

# Top 5 products by revenue
revenue_by_product = orders.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("=== Top products by revenue ===")
print(revenue_by_product.head(5))
print()

# Monthly revenue
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
orders["Month"] = orders["OrderDate"].dt.to_period("M").astype(str)
monthly_revenue = orders.groupby("Month")["Revenue"].sum().sort_values()
print("=== Monthly revenue ===")
print(monthly_revenue)
print()

# Plot 1: Revenue by country
revenue_by_country.sort_values().plot(kind="barh")
plt.title("Revenue by Country")
plt.xlabel("Revenue")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# Plot 2: Revenue by category
revenue_by_category.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Plot 3: Monthly revenue trend
monthly_revenue.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()