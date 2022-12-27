h, w = map(int, input().split())

if h < 2 or w < 2:
    ans = max(h, w)
else:
    x = 0--h//2
    y = 0--w//2
    ans = x * y

print(ans)
