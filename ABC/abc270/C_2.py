import sys
sys.setrecursionlimit(10**6)
n, x, y = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)


def dfs(crr, pre):
    if crr == y:
        return True
    for nxt in G[crr]:
        if nxt != pre:
            ans.append(nxt)
            if dfs(nxt, crr):
                return True
            ans.pop()
    return False

ans = [x]
dfs(x, -1)
print(*ans)



