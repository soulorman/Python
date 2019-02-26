#encoding: utf-8
languages = ['python', 'java', 'python', 'c', 'c++', 'go', 'c#', 'c++', 'lisp', 'c', 'javascript', 'java', 'python', 'matlab', 'python', 'go', 'java']

#result = {}

#for lang in languages:
 #   if lang not in result:
 #       result[lang] = 1
 #   else:
 #       result[lang] += 1
#print(result)

result = {}
for lang in languages:
    result[lang] = result.get(lang,0) + 1
#                  di yi ci wei 0   --> 0  +1
#                  di er ci wei  lang de valus 1  --> 1+1


result = {}
for lang in languages:
    result.setdefault(lang,0)
    result[lang] += 1


result = {}
for lang in languages:
    result[lang] = result.setdefault(lang,0) + 1





