def quick_sort(parm_list): 
    """快排 

    每次选取第一个值为基准值，再把列表中比基准值大的组成新列表，小的组成另一个新列表 再次对两个新列表进行操作，直到新列表为空
    :param parm_list: 参数列表 
    :return: 
    """
    if not parm_list: 
        return [] 
    else: 
        pivot = parm_list[0] 
        # 利用递归每次找出大于和小于基准值得两个新列表 
        lesser = quick_sort([x for x in parm_list[1:] if x < pivot]) 
        greater = quick_sort([x for x in parm_list[1:] if x >= pivot]) 
        # 最后将排列好的值相加 
        return lesser + [pivot] + greater 

if __name__ == '__main__': 
    demo_list = [4, 23, 5, 6, 43, 14, 9, -23, 2, 6, 123, 12, 3, 3, 3, 3, 1] 
    print(quick_sort(demo_list))
