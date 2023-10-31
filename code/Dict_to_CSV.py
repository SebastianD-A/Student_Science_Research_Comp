#small script to turn dict into csv again

import pandas

inputData = {'Jakarta Pusat': 694657, 'Jakarta Utara': 1146677, 'Jakarta Barat': 1187907, 'Jakarta Selatan': 2028618, 'Jakarta Timur': 1570279}
listCity = []
listAmount = [] 
for i in inputData:
    listCity.append(i)
    listAmount.append(inputData[i])

print(listCity)
print(listAmount)

df = pandas.DataFrame(list(zip(listCity, listAmount)), columns =['City', 'Amount'])
print(df)
df.to_csv("Roads.csv", index=False)