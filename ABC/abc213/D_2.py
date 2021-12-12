import sys
sys.setrecursionlimit(200000)
n = int(input())
G = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
ans = []
for i in range(n + 1):
    G[i].sort()
seen = [0] * (n + 1)

def dfs(v):
    seen[v] = 1
    ans.append(v)
    for nxt in G[v]:
        if not seen[nxt]:
            dfs(nxt)
            ans.append(v)


dfs(1)
print(*ans)
