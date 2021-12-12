import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n, a, b = map(int, input().split())
ans = 0
for i in range(1, n):
    ans += combinations_count(n, i)
for j in [a, b]:
    if j <= n:
        ans -= combinations_count(n, j)

print(ans % (10**9+7))