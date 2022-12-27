import sys 
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    G[x].append(y)

dp = [-1] * (n+1)

def f(v):
    if dp[v] >= 0:
        return dp[v]
    ret = 0
    for w in G[v]:
        ret = max(ret, f(w) + 1)
    dp[v] = ret
    return ret

ans = max(f(v) for v in range(1, n+1))
print(ans)

