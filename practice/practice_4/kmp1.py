# KMP算法

# 首先计算next数组，即我们需要怎么去移位
# 接着我们就是用暴力解法求解即可
# next是用递归来实现的
# 这里是用回溯进行计算的
def calNext(str2):
    i=0
    next=[-1]
    j=-1
    while(i<len(str2)-1):
        if(j==-1 or str2[i]==str2[j]):#首次分析可忽略
            i+=1
            j+=1
            next.append(j)
        else:
            j=next[j]#会重新进入上面那个循环
    return next
print(calNext('abcabx'))#-1,0,0,0,1,2

def KMP(s1,s2,pos=0):#从那个位置开始比较
    next=calNext(s2)
    i=pos
    j=0
    while(i<len(s1) and j<len(s2)):
        if(j==-1 or s1[i]==s2[j]):
            i+=1
            j+=1
        else:
            j=next[j]
    if(j>=len(s2)):
        return i -len(s2)#说明匹配到最后了
    else:
        return 0
s1 = "acabaabaabcacaabc"
s2 = "abaabcac"
print(KMP(s1,s2))
