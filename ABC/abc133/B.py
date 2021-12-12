n, d = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(n)]
def dist2(x, y, d):
    dist2 = 0
    for i in range(d):
        dist2 += (x[i] - y[i]) ** 2
    return dist2

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(1, 133):
            if dist2(X[i], X[j], d) == k ** 2:
                ans += 1
print(ans)
