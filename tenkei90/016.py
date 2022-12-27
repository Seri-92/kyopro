n = int(input())
a, b, c = map(int, input().split())
ans = 10000
for s in range(10000):
    for t in range(10000-s):
        remain = n - a * s - b * t
        if remain < 0:
            continue
        if remain % c == 0:
            u = remain // c
            ans = min(ans, s + t + u)

print(ans)
