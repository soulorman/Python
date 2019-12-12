def test(s):
    stack = 0
    num = 0
    for i in s:
        if i == "L":
            stack += 1
        else:
            stack -= 1
        if stack == 0:
            num += 1

    return num

s = "LLLLRRRR"
print(test(s))
