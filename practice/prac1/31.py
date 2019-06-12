#enconding: utf-8

g_a = 1
g_b = [1]
g_c = [1]


def change(a,b,c):
    a = 2
    b = [1,2]
    c.append(2)
    print(a,b,c)
change(g_a, g_b, g_c)
print(g_a,g_b,g_c)



