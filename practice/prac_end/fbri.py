# encoding: utf-8

fibs = [0, 1]
num = int(input('how long?'))
for i in range(num - 2):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)
