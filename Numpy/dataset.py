import numpy as np
import matplotlib.pyplot as plt

# Data Structure : [restaurant_id , 2021 , 2022 , 2023, 2024]
sales_data = np.array([
    [1,15000,180000,220000,250000],  # [aradise iryani
    [2,120000,140000,160000,190000], # Beijing Bites
    [3,200000,230000,260000,300000], # Pizza Hub
    [4,180000,210000,240000,270000], # Burger Point
    [5,160000,185000,205000,230000]  # Chai Point
])

print("=== Zomato sales analysis ===")
print("\n Sales data shape",sales_data.shape)
print("\n Sample data for 1st 3 restaurant:", sales_data[0:3])

# total sales per year

print(np.sum(sales_data,axis=0))
yearly_total = np.sum(sales_data[:, 1:], axis=0)
print("Yearly total sales:",yearly_total)

# Minimum sales per restaurant

min_sales = np.min(sales_data[:, 1:], axis=1)
print("Minimum sales per restaurant:",min_sales)

# Maximum sales per year

max_sales = np.max(sales_data[:,1:], axis =0)
print("Maximum sales per year:",max_sales)

# Min sales per restaurant
min_sales = np.min(sales_data[:,1:],axis=1)
print("Minimum sales per restaurant:",min_sales)

# Maximum sales per year
max_sales = np.max(sales_data[:, 1:],axis=0)
print("Maximum sales per year:",max_sales)

# Average sales per restaurant
avg_sales = np.mean(sales_data[:,1:],axis=1)
print("Average sales are:",avg_sales)

cumsum =np.cumsum(sales_data[:,1:],axis=1)
print(cumsum)

# plt.figure(figsize=(10, 6))
# plt.plot(np.mean(cumsum,axis=0))
# plt.title("Average cumilative sales accross all restaurant")
# plt.xlabel("years")
# plt.ylabel("Sales")
# plt.grid(True)
# plt.show()

vector1 = np.array([1,2,3,4,5])
vector2 = np.array([6,7,8,9,10])
print("Vector addition:",vector1 + vector2)
print("\n Multiplication vector:", vector1 * vector2)
print("\n Dot Product:", np.dot(vector1,vector2))
# print("\n cross product of n:", np.cross(vector1,vector2))
