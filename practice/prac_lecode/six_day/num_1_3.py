def test(nums, target):
    hashmap = {}
    for idx, num in enumerate(nums):
        hashmap[num] = idx

    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]

nums = [3,2,4]
target = 6
print(test(nums, target))

