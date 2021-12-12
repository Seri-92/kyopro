import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n, m = map(int, input().split())

if n < 2:
    if m < 2:
        ans = 0
    else:
        ans = combinations_count(m, 2)
else:
    if m < 2:
        ans = combinations_count(n, 2)
    else:
        ans = combinations_count(n, 2) + combinations_count(m, 2)
print(ans)