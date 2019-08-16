import pandas as pd
import matplotlib.pyplot as plt

tables = pd.read_csv('./train.csv')
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

testTable = table[(table["land_area"] <= 2000) & (table["total_price"] <= 300000000) & (table["building_area"] <= 1000)]
plt.scatter(testTable["building_area"] , testTable["total_price"])
plt.title("Building Area - After")
plt.xlabel("building_area")
plt.ylabel("total_price")
plt.show()
plt.scatter(testTable["land_area"], testTable["total_price"])
plt.title("Land Area - After")
plt.xlabel("land_area")
plt.ylabel("total_price")
plt.show()

table = table.drop(table[table["building_area"]>1000].index)
table = table.drop(table[table["total_price"]>300000000].index)
table = table.drop(table[table["land_area"]>2000].index)
plt.scatter(table["building_area"] , table["total_price"])
plt.title("Building Area - After")
plt.xlabel("building_area")
plt.ylabel("total_price")
plt.show()
plt.scatter(table["land_area"], table["total_price"])
plt.title("Land Area - After")
plt.xlabel("land_area")
plt.ylabel("total_price")
plt.show()

#print(table["land_area"]<10)
#print(table[table["land_area"]<10].index)