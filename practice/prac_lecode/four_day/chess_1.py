
def  test(n):
    ans = 0
    if len(points) >= 1 and len(points) <= 100 and len(points[0]) == 2:
        x0, y0 = points[0]
        if x0 >= -1000 and y0 <= 1000:
            for i in range(1, len(points)):
                if len(points[i]) == 2:
                    x1, y1 = points[i]
                    if x1 >= -1000 and y1 <= 1000:
                        ans += max(abs(x0-x1),abs(y0-y1))
                        x0, y0 = points[i]
                    else:
                        ans = False
                        break
                else:
                    ans = False
                    break

    return ans

points = [[1,1],[-10001,900],[-1,0]]
print(test(points))
