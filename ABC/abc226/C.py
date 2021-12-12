import sys
sys.setrecursionlimit(220000)
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def dfs(v):
    visited[v] = 1
    root.append(v)
    if a[v-1][1] == 0:
        return
    for w in sorted(a[v-1][2:]):
        if visited[w]:
            continue
        dfs(w)
 
visited = [0] * (n + 1)
root = []
dfs(n)
ans = 0
for i in range(len(root)):
    ans += a[root[i] - 1][0]

print(ans)