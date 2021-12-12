n, k = map(int, input().split())
k = abs(k)
ans = 0
for i in range(2, 2*n+1):
    if n + 1 < i:
        a = i - 1 - 2 * (i - n - 1)
    else:
        a = i - 1
    if 2 <= i+k and i+k <= 2*n:
        if n + 1 < i + k:
            b = i + k - 1 - 2 * (i + k - n - 1)
        else:
            b = i + k - 1
        ans += a * b
print(ans)