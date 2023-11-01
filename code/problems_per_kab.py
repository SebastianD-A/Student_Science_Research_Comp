import pandas as pd
from collections import Counter

data= pd.read_csv("original CRM Data.csv")

problems= data.iloc[:, 3].astype(str)
problem_status= data.iloc[:, 2].astype(str)
problems_area= data.iloc[:, 8].astype(str)

#listed
problems_listed = problems.tolist()
problems_status_listed = problem_status.tolist()
problems_area_listed = problems_area.tolist()

#areas
jaksel = []
jakbar = []
kabser = []
jaktim = []
jakut = []
jakpus = []


for i in range(len(problems_status_listed)):
    if (problems_status_listed[i] != "Selesai"):
        problems_listed.pop()
        problems_area_listed.pop()

for i in range(len(problems_area_listed)):
    match problems_area_listed[i]:
        case "KAB.ADM.KEP.SERIBU":
            kabser.append(problems_listed[i])
        case "JAKARTA PUSAT":
            jakpus.append(problems_listed[i])
        case "JAKARTA BARAT":
            jakbar.append(problems_listed[i])
        case "JAKARTA TIMUR":
            jaktim.append(problems_listed[i])
        case "JAKARTA SELATAN":
            jaksel.append(problems_listed[i])
        case "JAKARTA UTARA":
            jakut.append(problems_listed[i])

kabser_count = Counter(kabser)
jakpus_count = Counter(jakpus)
jakbar_count = Counter(jakbar)
jaktim_count = Counter(jaktim)
jaksel_count = Counter(jaksel)
jakut_count = Counter(jakut)

print("Kabupaten Administrasi Kepulauan Seribu:")
for problem, count in kabser_count.items():
     print(f"{count}")
print()
print("Jakarta Pusat:")
for problem, count in jakpus_count.items():
     print(f"{count}")
 print()
print("Jakarta Barat:")
for problem, count in jakbar_count.items():
     print(f"{count}")
 print()
print("Jakarta Timur:")
for problem, count in jaktim_count.items():
     print(f"{count}")
print()
print("Jakarta Selatan:")
for problem, count in jaksel_count.items():
     print(f"{count}")
 print()
print("Jakarta Utara:")
for problem, count in jakut_count.items():
    print(f"{count}")