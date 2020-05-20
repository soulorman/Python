def quick_sort(L, left, right):
  if left >= right:
    return
  stack = []
  stack.append(left)
  stack.append(right)
  while stack:
    low = stack.pop(0)
    high = stack.pop(0)
    if high - low <= 0:
      continue
    x = L[high]
    i = low - 1
    for j in range(low, high):
      if L[j] <= x:
        i += 1
        L[i], L[j] = L[j], L[i]
    L[i + 1], L[high] = L[high], L[i + 1]
    stack.extend([low, i, i + 2, high])


a = [3,2,1]
quick_sort(a,0,len(a)-1)
print(a)

