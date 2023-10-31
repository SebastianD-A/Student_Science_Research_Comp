import pandas as pd 
from collections import Counter

data= pd.read_csv("original CRM Data.csv")

problems= data.iloc[:, 3].astype(str).tolist()
problem_status= data.iloc[:, 2].astype(str).tolist()

for i in range(len(problem_status)):
    if (problem_status[i] != "Selesai"):
        problems.pop()

problem_count = Counter(problems)
for problem, count in problem_count.items():
    print(f"{problem}")

