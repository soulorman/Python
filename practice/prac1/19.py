#encoding: utf-8


nums_1 = [1,2,3,4,5,3,10,11]
nums_2 = [1,2,3,1,4,5,5,3,12,34]

nums = set(nums_1) & set(nums_2)
print(list(nums))
