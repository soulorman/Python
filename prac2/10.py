#enconding；utf-8



num1 = [1,2,3,4,5,6,7,8,9]
num2 = [1,2,7,8,11,1230]

result = []



for num in num1:
    if num  in num2 and num not in result:
        result.append(num)



#        result.append(num)
print(result)


