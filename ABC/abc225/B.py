n = int(input())
t = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    t[a].append(b)
    t[b].append(a)
l = []
for i in range(1, n+1):
    l.append(len(t[i]))
if max(l) < n - 1:
    print('No')
else:
    print('Yes')
    