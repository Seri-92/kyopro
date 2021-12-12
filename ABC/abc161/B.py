n, m = map(int, input().split())
a = list(map(int, input().split()))
popular = 0
for i in range(n):
    if a[i] >= sum(a) / (4 * m):
        popular += 1

print("Yes" if popular >= m else 'No')