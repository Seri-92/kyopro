n = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    sa = lst[i-1] - lst[i]
    if sa > 0:
        ans += sa
        lst[i] = lst[i-1]
print(ans)