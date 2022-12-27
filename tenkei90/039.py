import sys
sys.setrecursionlimit(10**7)
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)



# count subordinate vertex
dp = [0] * (n+1)

def dfs(crr, pre):
    num_tmp = 1
    for nxt in tree[crr]:
        if nxt == pre:
            continue
        num_tmp += dfs(nxt, crr)
    dp[crr] = num_tmp
    return num_tmp
        
dfs(1, -1)

ans = 0
for i in range(1, n+1):
    ans +=  dp[i] * (n-dp[i])

print(ans)
