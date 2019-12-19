# 核心思想
# 对比相邻的两个数，一样就不管，不一样就互相换位置（已排好序）。。。感觉很新奇的想法
def test(nums):
    if len(nums) == 0:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


nums = [0,0,1,1,1,2,2,3,3,4]
print(test(nums))
