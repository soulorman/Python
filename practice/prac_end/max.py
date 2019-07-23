#encoding: utf-8

nums = [5, 8, 7, 10, 20, 2, 6, 9]

max_index = 0
idx = 0

for num in nums:
    if num > nums[max_index]:
        max_index = idx
    idx += 1

print(max_index,nums[max_index])
