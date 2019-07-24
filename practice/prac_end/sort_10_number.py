# encoding: utf-8

article = 'I was not delivered unto this world in defeat, nor does failure course in my veins. I am not a sheep waiting to be prodded by my shepherd. I am a lion and I refuse to talk, to walk, to sleep with the sheep. I will hear not those who weep and complain, for their disease is contagious. Let them join the sheep. The slaughterhouse of failure is not my destiny.'
result = {}

for ch in article:
    if ch.isalpha():
        result[ch] = result.get(ch, 0) + 1

list_result = list(result.items())

for i in range(len(list_result) - 1):
    for j in range(len(list_result) - 1):
        if list_result[j][1] > list_result[j+1][1]:
            list_result[j],list_result[j+1] = list_result[j+1],list_result[j]

for idx, e in enumerate(list_result[:-11:-1]):
    ch, cnt = e
    print(idx+1,':', ch,':',cnt)
