# To read the file 

# import csv

# with open ('sample.csv') as f:
#     f_csv=csv.reader(f)
#     headers=next(f_csv)
#     print(headers)
#     for row in f_csv:
#         print(row)



# To write the file

# import csv

# with open("students.pdf", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["ID", "Name", "Age", "Course"])
#     writer.writerow([1, "Vishal", 23, "B.Tech CSE"])
#     writer.writerow([2, "Rahul", 22, "BCA"])
#     writer.writerow([3, "Priya", 21, "MCA"])

import json

data = [
    {'name': 'IRFC',
    'shares': '100',
    'price': '95'},
    {'name': 'Wipro',
    'shares': '90',
    'price': '178'},
    {'name': 'IREDA',
    'shares': '100',
    'price': '125'}
]
with open('data.json','w') as f:
    json.dump(data,f)
with open('data.json','r') as f:
    data=json.load(f)
    print(data)