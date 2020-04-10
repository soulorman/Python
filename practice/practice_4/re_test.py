#!/usr/bin/python3
import re

html_str = '<html><h1><div>a="张明 98 分"</div></html>'
result_str = re.sub(r'\d{2,}', '100', html_str)
print(result_str)

demo_str = "abcdacsdn" 
print("原始字符串 " + demo_str) 


# 非贪婪匹配
non_greedy = "a.*?d" 
print("非贪婪匹配 = " + non_greedy) 
pattern = re.compile(non_greedy) 
restult_list = re.findall(pattern , demo_str) 
print("非贪婪匹配") 
print(restult_list) 

# 贪婪匹配 
greedy = "a.*d"
print("贪婪匹配 = " + greedy) 
pattern = re.compile(greedy) 
restult_list = re.findall(pattern , demo_str) 
print("贪婪匹配结果") 
print(restult_list)
