#encoding: utf-8
article = 'I was not delivered unto this world in defeat, nor does failure course in my veins. I am not a sheep waiting to be prodded by my shepherd. I am a lion and I refuse to talk, to walk, to sleep with the sheep. I will hear not those who weep and complain, for their disease is contagious. Let them join the sheep. The slaughterhouse of failure is not my destiny.' 

result = {}

chars = 'abcdefghijklmnopqrstuvwxyz'
chars += chars.upper()

for ch in article:
    cnt = article.count(ch)
    if cnt:
            result[ch] = cnt

result_list = list(result.items())

for j in range(len(result_list)-1):
    for i in range(len(result_list)-1):
        if result_list[i][1] > result_list[i+1][1]:
            result_list[i],result_list[i+1] = result_list[i+1],result_list[i]

for idx,e in enumerate(result_list[-1:-11:-1]):
    ch,cnt =e
    print(idx+1,":",ch,":",cnt)
