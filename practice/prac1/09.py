#encoding:utf-8

jobs = []

while True:
    prompt = input('请输入任务/do: ')
    if prompt == 'do':
        if jobs:
            print('请完成任务',jobs.pop(0))
        else:
            print('任务已完成')
            break
    else:
        jobs.append(prompt)
