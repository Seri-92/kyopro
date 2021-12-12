n, k = map(int, input().split())
s = set()
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
        s.add(j)
print(n - len(s))
    