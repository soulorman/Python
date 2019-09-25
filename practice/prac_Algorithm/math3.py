# encoding: utf-8

sum = 0

i=1

while i<1000:
    j=0
    while j<1000:
        sum += 1
        j += 1
    i *= 2

print(sum)
