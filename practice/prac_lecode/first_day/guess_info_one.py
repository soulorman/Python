# enconding: utf-8

def guess_info(guess, answer):
    result = 0

    for tuple_num in zip(guess, answer):
        if len(set(tuple_num)) == 1:
            result += 1
    
    return result

guess = [2,2,1]
answer = [3,2,1]

print(guess_info(guess, answer))
