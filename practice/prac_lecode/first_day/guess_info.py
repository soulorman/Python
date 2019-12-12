# 题目描述

#小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？
#输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。

#限制：
#guess的长度 = 3
#answer的长度 = 3
#guess的元素取值为 {1, 2, 3} 之一。
#answer的元素取值为 {1, 2, 3} 之一。

#enconding: utf-8

def guess_info(guess, answer):
    result = 0

    if len(guess) == 3 and len(answer) == 3:
        for i in range(len(guess)):
            if isinstance(guess[i],int) and isinstance(answer[i],int):
                if guess[i] < 4 and guess[i] > 0 and answer[i] < 4 and answer[i] > 0:
                    if guess[i] == answer[i]:
                        result += 1
                else:
                    break
            else:
                break

    return result

guess = [2,2,3]
answer = [3,2,1]

print(guess_info(guess, answer))
