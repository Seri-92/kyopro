import sys
sys.setrecursionlimit(300000)

n = int(input())
def dfs(v):
    visited[v] = 1
    ans.append(v)
    for w in sorted(G[v]):
        if visited[w]:
            continue
        dfs(w)
        ans.append(v)
G = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [0] * (n + 1)
ans = []
dfs(1)
print(*ans)

