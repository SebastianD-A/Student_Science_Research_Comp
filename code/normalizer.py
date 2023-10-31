Cleaned = "80.29 82.66 84.72 81.38 81.38".split()
print(Cleaned)
Real = []
for i in Cleaned:
  Real.append(float(i))
print(Real)

Minimum= min(Real)
Maximum= max(Real)
New = []

for i in Real:
  New.append((i-Minimum)/(Maximum-Minimum))

for i in New:
  print(i)
