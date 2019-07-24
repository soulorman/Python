# encoding: utf-8

languages = ['python', 'java', 'python', 'c', 'c++', 'go', 'c#', 'c++', 'lisp', 'c', 'javascript', 'java', 'python', 'matlab', 'python', 'go', 'java']

result = {}

for lang in languages:
    if lang not in result:
        result[lang] = 1
    else:
        result[lang] += 1
print(result)

# 优化版
for lang in languages:
    result[lang] = result.get(lang, 0) + 1
    
print(result)
