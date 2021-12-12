r, x, y = map(int, input().split())
l = x**2 + y**2
for m in range(300000):
    if l / (r**2) <= m**2:
        print(m)
        exit()