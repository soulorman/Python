# 核心思路
# 建立两个指针，一个从开始指一个，另一个指下一个，一样就弹出第二个，不一样就递增
# 反思一下  这么简单的想法，为什么我就没想到？？？
def test(nums):
    pre = 1
    while  pre < len(nums):
        if nums[pre-1] == nums[pre]:
            nums.pop(pre)
        else:
            pre = pre + 1

     return len(nums)



nums = [0,0,1,1,1,2,2,3,3,4]
print(test(nums))
