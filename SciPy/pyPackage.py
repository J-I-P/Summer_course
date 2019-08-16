import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tables = pd.read_csv('train.csv')
totalPrice = tables["total_price"]
buildingArea = tables["building_area"]
landArea = tables["land_area"]

table = tables.loc[:,['building_area', 'land_area', 'total_price']]

plt.scatter(table['building_area'], table['total_price'])
plt.title("Building Area - Before")
plt.xlabel("building_area")
plt.ylabel("total_price")
plt.show()
plt.scatter(table['land_area'], table['total_price'])
plt.title("Land Area - Before")
plt.xlabel("land_area")
plt.ylabel("total_price")
plt.show()


buildingArea_table = table[(table["building_area"] <= 1000) & (table["total_price"] <= 300000000)]
landArea_table = table[(table["land_area"] <= 2000) & (table["total_price"] <= 300000000)]
plt.scatter(buildingArea_table["building_area"] , buildingArea_table["total_price"])
plt.title("Building Area - After")
plt.xlabel("building_area")
plt.ylabel("total_price")
plt.show()
plt.scatter(landArea_table["land_area"], landArea_table["total_price"])
plt.title("Land Area - After")
plt.xlabel("land_area")
plt.ylabel("total_price")
plt.show()