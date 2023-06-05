import csv
import pandas as pd
d=[]
data = pd.read_csv("dwarf_stars.csv")

# print(data.shape) # (352, 5)
newdata=data.dropna()
for i in newdata:
    d.append(i)
header=d[0]
stardatarows=d[1:]
print(stardatarows)
star_mass=[]
star_radius=[]
for i in stardatarows:
  star_radius.append(i[3])
  star_mass.append(i[2])
star_mass=float(star_mass)*0.000954588
star_radius=float(star_radius)*0.102763
newdata.to_csv('archive_dataset.csv')
