# -*- coding: utf-8 -*-
"""LVADSUSR82.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xBt_SbuqfqnlxoX0fOJj08FQx2ke45ft
"""

#1
import numpy as np
rgb_array=np.array[[[100,0,0],[0,100,0],[0,0,100]],[[100,100,0],[100,0,100],[0,100,100]],[[250,250,250],[57,57,57],[150,150,150]]]

def rgbtograyscale(rgb_array,r,g,b):
  r=rgb_array[1,1]
  g=rgb_array[1,2]
  b=rgb_array[1,3]
  rgb_array=rgbtograyscale.rgb_array

rgbtograyscale()

#2
import numpy as np
def mean(health_data):
  meandata=health_data[1]+health_data[2]+health_data[3]

def std_deviation(health_data):
  pass

health_data=[[['height','weight','age'],['height','weight','age']],[['height','weight','age'],['height','weight','age']]]
for i in health_data:
  health_data[i,1]=int(input("enter the height"))

for i in health_data:
  health_data[i,2]=int(input("enter the weight"))

for i in health_data:
  health_data[i,3]=int(input("enter the age"))

mean()
std_deviation()

#3
import pandas as pd

data = {'A':[13.2, 14.2, 13.5, 13.6, 14.3], 'B':{'C':[10.2,10.4,10.6,10.7,10.8],'D':[6.5,5.4,6.7,6.6,6.5]}}
df = pd.DataFrame({'pH_sensor': data['A'], 'Ions': data['B']['C'], 'Connectivity': data['B']['D']})
df

#4
import numpy as np
arr=np.array([[[10,20,30],[11,8,23]],[[12,23,33],[4,0,67]]])

if arr[0,0]>arr[0,2]:
  print("player 1 has improved")
elif arr[1,0]>arr[1,2]:
  print("player 2 has improved")
elif arr[2,0]>arr[2,2]:
  print("player 3 has improved")
elif arr[3,0]>arr[3,2]:
  print("player 4 has improved")

#10
import pandas as pd
data={'Department':['Electronics','Electronics','clothing','clothing','homegoods']
      'salesperson':['alice','bob','charlie','david','eve']
      'sales':[70000,50000,30000,40000,60000]}

df=pd.dataframe(data)
def averagesaleselectronics(data):
  averagesalesofelectronics=df.data[2,0]+df.data[2,1]/2
  print(averagesalesofelectronics)

def averagesalesclothing(data):
  averagesalesofclothing=df.data[2,2]+df.data[2,3]/2
  print(averagesalesofclothing)

def averagesaleshomegoods(data):
  averagesalesofhomegoods=df.data[2,4]/1
  print(averagesalesofhomegoods)

averagesaleselectronics()
averagesalesclothing()
averagesaleshomegoods()

#5
import pandas as pd

climate_data = {
    'City': ['London', 'London', 'Paris', 'Paris', 'Belgium', 'Belgium', 'Stockholm', 'Stockholm'],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
    'AverageTemperature': [7, 6, None, 5, 4, None, None, 3],
    'Precipitation': [5, None, 2, 4, 2, 3, 2, 4]
}

climate_df = pd.DataFrame(climate_data)

climate_df['AverageTemperature'] = climate_df.groupby('City')['AverageTemperature'].transform(lambda x: x.fillna(x.mean()))

climate_df['Precipitation'].fillna(0, inplace=True)

print(climate_df)

#7
import pandas as pd

sales_data = {
    'StoreID': [1, 1, 2, 2, 3, 4, 5, 6],
    'Product': ['Phones', 'Headphones', 'Smartwatches', 'iPad', 'Headphones', 'Smartwatches', 'iPad', 'Phones'],
    'Month': ['January', 'January', 'February', 'February', 'March', 'March', 'April', 'April'],
    'SalesAmount': [100000, 40000, 60000, 400000, 30000, 40000, 600000, 500000]
}

sales_df = pd.DataFrame(sales_data)

pivot_table = sales_df.pivot_table(index='Product', columns='Month', values='SalesAmount', aggfunc='sum')

pivot_table.fillna(0, inplace=True)

print(pivot_table)

