# encoding: utf-8

t = 9.0

while (abs(t - 9.0/t) > .001): 
    t = (9.0/t + t) / 2.0

print(t)
