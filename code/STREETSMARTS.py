import pandas

data= pandas.read_csv("jalanpanjang.csv")
StreetDict = {}

for i in range(len(data)):
    if StreetDict.get(data.iat[i,0])!=None :
        StreetDict.update({data.iat[i,0]:data.iat[i,2]+StreetDict.get(data.iat[i,0])})
    else:
        StreetDict.update({data.iat[i,0]:data.iat[i,2]})
print(StreetDict)
