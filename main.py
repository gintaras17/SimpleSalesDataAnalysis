import pandas as pd
import matplotlib.pyplot as plt

#paprastas duomenu apie pardavimus traukimas, tvarkymas ir statistikos perziura

# ikeliu duomenis
df = pd.read_csv("C:/Users/ginta/PycharmProjects/SimpleSalesDataAnalysis/sales_data.csv")

# print(df.head())

#patikrinu del klaidu ir paziuriu skaiciu statistika
#print(df.info())
# print(df.describe())

# patikrinu del trukstamu reiksmiu
# print(df.isnull().sum())

#sukuriu nauja stulpeli
df["Total"] = df["Quantity"] * df["Price"]

#darbas su datomis
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Month"] = df["OrderDate"].dt.month

monthly_sales = df.groupby("Month")["Total"].sum()

# print(monthly_sales)
city_sales = df.groupby("City")["Total"].sum()

# print(city_sales)

product_sales = df.groupby("Product")["Quantity"].sum()

# print(product_sales)

monthly_sales.plot(kind="bar")

plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Revenue")

# plt.show()

product_sales.plot(kind="bar")

plt.title("Product Popularity")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

# plt.show()

product_sales.plot(kind="bar")

plt.title("Product Popularity")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

# plt.show()

avg_order = df["Total"].mean()

# print("Average order value:", avg_order)

