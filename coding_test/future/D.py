import sys
sys.setrecursionlimit(10**7)
n, m, l = map(int, input().split())
g_list = list(map(int, list('0' + input())))
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v, d = map(int, input().split())
    graph[u].append([v, d])
    graph[v].append([u, d])

def dfs(v, gas):
    visited[v] = 1
    if g_list[v]:
        ans.append(v)
    else:
        if gas >= l / 2:
            ans.append(v)
    for w, d in graph[v]:
        if visited[w]:
            continue
        if gas < d:
            continue

        if g_list[w]:
            dfs(w, l)
        else:
            dfs(w, gas-d)
        

visited = [0] * (n+1)
ans = []
dfs(1, l)
print(len(ans))
