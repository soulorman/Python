s = 'abcabcabcffadabc'
start = 0
while True:
    pos = s.find('abc',start)
    if pos == -1:
       break
    print(pos)
    start= pos + 1
