x, y = map(int, input().split())
if x % y == 0:
    print(-1)
    exit()
else:
    print(x)