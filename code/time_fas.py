import pandas as pd
from collections import Counter

data= pd.read_csv("original CRM Data.csv")

month = (data.iloc[:, 9].astype(str)).tolist()
problem = (data.iloc[:, 3].astype(str)).tolist()

month_used = []
year_used = []
month_2022=[]
month_2023=[]

#filter to fasos/fasum
for i in range(len(problem)):
    if problem[i]=="Fasilitas Sosial/Fasilitas Umum (Fasos/Fasum)":
        month_used.append(month[i])

for i in range(len(month_used)):
    year_used.append(month_used[i][0:4])
    month_used[i] = (month_used[i][5:7])

for i in range(len(month_used)):
    if year_used[i]=="2022":
        month_2022.append(month_used[i])
    else:
        month_2023.append(month_used[i])

for month,count in (Counter(month_2022).items()):
    print(f"{month},{count}")
    
for month,count in (Counter(month_2023).items()):
    print(f"{month},{count}")
    