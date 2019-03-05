#encondig: utf-8
total = 0
count = 0
prompt = ''

while   prompt != 'exit':
    prompt = input("请输入数字或者EXIT： ")
    if prompt != 'exit':
        total += float(prompt)
        count += 1

if count != 0:
    print('结果是:',total,',平均数',total / count)
else:
    print('结果是:',total,',平均数是0')
