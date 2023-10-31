import pandas as pd
import datetime

averageTime={}

updatedData=pd.read_csv("output.csv")

for i in range(len(updatedData)):
  if averageTime.get(updatedData.iat[i,3])!=None:
    averageTime.update({updatedData.iat[i,3]:datetime.datetime(+updatedData.iat[i,11])}) 
    averageTime.update({f"{updatedData.iat[i,3]} Amount" : averageTime[f"{updatedData.iat[i,3]} Amount"]+1})
  else:
    averageTime.update({updatedData.iat[i,3]:updatedData.iat[i,11]}) 
    averageTime.update({f"{updatedData.iat[i,3]} Amount" :1})

print(averageTime.items())
