import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv('Book1.csv')
print(f"Original Data: \n {data} \n")

info=data.drop_duplicates().dropna().reset_index(drop=True)
print(f"Data After Cleaning: \n {info} \n")
print(f"Statistical Review: \n{info.describe()} \n")
plt.figure(figsize=(11.5,8))
plt.hist(info['Income'],color='pink', alpha=0.5, edgecolor='black', label='Income')
plt.hist(info['Expenditure'], color='lightgreen', alpha=0.5, edgecolor='black', 
label='Expenditure')
plt.title("Income VS Expenditure\n")
plt.ylabel('Frequency\n')
plt.xlabel('\nIncome & Expenditure')
plt.legend()
plt.show()

print("Regional Data Insights:\n")

regions = info['Region'].unique()
for region in regions:
    region_data = info[info['Region'] == region]
    
    if region_data['Income'].duplicated().any():
        print(f"Overlapping Income data in {region} region\n")
    if region_data['Expenditure'].duplicated().any():
        print(f"Overlapping Expenditure data in {region} region\n")
    print(f"Data for {region}: \n{region_data}\n")
