def quick_sort_3(l):
    if len(l) <= 1: return l
    return quick_sort_3([lt for lt in l[1:] if lt < l[0]]) + l[0:1]+ quick_sort_3([ge for ge in l[1:] if ge >= l[0]])
print(quick_sort_3([3,2,9]))
