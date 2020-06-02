
import csv

with open('data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)

    for i in reader:
        print(i)
