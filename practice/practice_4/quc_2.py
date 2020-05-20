def quick_sort_2(l):
    if len(l) <=1:
        return l
    else:
        key = l[0]
        left =  [ e for e in l[1:] if e <= key ]
        right =  [ e for e in l[1:] if e > key ]
        return quick_sort_2(left) + [key] + quick_sort_2(right)

print(quick_sort_2([3,2,9]))
