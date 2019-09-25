# encoding: utf-8

text = input("请输入三个数: ")

List = text.split(",")

if int(List[0]) == int(List[1]) and int(List[1]) == int(List[2]):
    print("equal")
else:
    print("no equal")
