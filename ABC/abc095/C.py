a, b, c, x, y = list(map(int, input().split()))
c *= 2
lst = []
for i in range(max(x, y)+1):
    cst = c * i + a * max(0, x - i) + b * max(0, y - i)
    lst.append(cst)
print(min(lst))

