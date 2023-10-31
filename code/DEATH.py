import pandas

data= pandas.read_csv("Sehat.csv")
Hospitaldict = {}

Cities= data.iloc[:, 0].astype(str).tolist

for i in range(len(data)):
    if Hospitaldict.get(data.iat[i,1])!=None :
        Hospitaldict.update({data.iat[i,1]:data.iat[i,4]+Hospitaldict.get(data.iat[i,1])})
    else:
        Hospitaldict.update({data.iat[i,1]:data.iat[i,4]})
print(Hospitaldict)
