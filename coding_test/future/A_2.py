n, a, m, k = map(int, input().split())

ans = 0
if m >= n * k:
    while m / (n + ans) > k:
        ans += 1

else:
    while (m + ans * a) / (n + ans) < k:
        ans += 1

print(ans)
