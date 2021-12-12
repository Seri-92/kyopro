x, n = map(int, input().split())
P = set(map(int, input().split()))

ans = 10 ** 10

for i in range(100):
    if not x - i in P:
        ans = x - i
    else:
        if not x + i in P:
            ans = x + i
    if ans < 10 ** 10:
        print(ans)
        exit()