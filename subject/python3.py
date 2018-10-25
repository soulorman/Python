#encoding: utf-8
score = int(input('please input score: '))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
print('%d belong %s' % (score,grade))
