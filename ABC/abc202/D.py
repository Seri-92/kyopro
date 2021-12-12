a, b, k = map(int, input().split())
n = b + 1
i = 0
while True:
    for j in range(n):
        m = n - j - i
        if k < m:
            break
        k -= m
    i += 1

while True:
    m = n * (n+1) // 2
    if k < m:
        break
    k -= m
    j += 1
