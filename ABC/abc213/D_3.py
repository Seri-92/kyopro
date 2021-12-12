n = int(input())
G = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(n+1):
    G[i].sort()
    
seen = [0] * (n + 1)
todo = [1]

