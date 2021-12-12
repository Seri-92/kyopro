n = int(input())
ans = 1e9
for _ in range(n):
    a, p, x = map(int, input().split())
    if x - a > 0:
        ans = min(ans, p)
if ans == 1e9:
    ans = -1
print(ans)

