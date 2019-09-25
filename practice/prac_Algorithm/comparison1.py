# encoding: utf-8

text = input("请输入两个数: ")

List = text.split(",")

if (float(List[0]) > 0 and float(List[0]) < 1) and (float(List[1]) > 0 and float(List[1]) < 1): 
    print("true")
else:
    print("false")
