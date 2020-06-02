import csv

header = ['name', 'password', 'status']

data = [
    {'name':'abc', 'password':'123456', 'status':'PASS'},
    {'name':'张五', 'password':'123#456', 'status':'PASS'},
    {'name':'张#abc123', 'password':'123456', 'status':'PASS'},
    {'name':'666', 'password':'123456', 'status':'PASS'},
    {'name':'a b', 'password':'123456', 'status':'PASS'}
]


with open('result2.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, header)
    writer.writeheader()
    writer.writerows(data)
