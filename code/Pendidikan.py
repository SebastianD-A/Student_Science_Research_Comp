from collections import Counter
import pandas as pd

data = pd.read_csv("data_pendidikan.csv")

city= (data.iloc[:,0].astype(str)).tolist()
peraih = (data.iloc[:,2].astype(str)).tolist()

prov=[]
mandiri=[]
kota=[]
nasional=[]

for i in range(len(city)):
    match peraih[i]:
        case "Peraih tingkat Provinsi":
            prov.append(city[i])
        case "Peraih tingkat Mandiri":
            mandiri.append(city[i])
        case "Peraih tingkat Kota":
            kota.append(city[i])
        case "Peraih tingkat Nasional":
            nasional.append(city[i])

prov_count=Counter(prov)
mandiri_count=Counter(mandiri)
kota_count=Counter(kota)
nasional_count=Counter(nasional)

print("Tingkat Provinsi:")
for area,count in prov_count.items():
    print(f"{area}: {count}")
print("Tingkat Mandiri:")
for area,count in mandiri_count.items():
    print(f"{area}: {count}")
print("Tingkat Kota:")
for area,count in kota_count.items():
    print(f"{area}: {count}")
print("Tingkat Nasional:")
for area,count in nasional_count.items():
    print(f"{area}: {count}")