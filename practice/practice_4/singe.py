a= [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
length = len(a)
for i in range(length - 1):
    for j in range(1, length): 
        if a[i] == a[j]:
            break
        
        if j == length-1:
            test = a[i]
print(test)

