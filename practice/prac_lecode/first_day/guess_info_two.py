#enconding: utf-8

def guess_info(guess, answer):
    result = 0

    if len(guess) == 3 and len(answer) == 3:
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                result += 1

    return result

guess = [1,2,3]
answer = [1,2,3]

print(guess_info(guess, answer))
