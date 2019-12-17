def test(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None:
            # 因为上面的循环要比下面赋值的快一步 所以这里反过来
            return [j, i]
        hashmap[num] = i

nums = [3, 2, 4]
target = 6
print(test(nums, target))
