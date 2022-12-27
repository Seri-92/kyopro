import sys
sys.setrecursionlimit(10**7)
n = int(input())
G = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [0] * (n+1)

def dfs(crr, pre=-1):
    for nxt in G[crr]:
        if nxt == pre: continue
        dist[nxt] = dist[crr] + 1
        dfs(nxt, crr)

dfs(1)
    
node_list = [[], []]

for i in range(1, n+1):
    node_list[dist[i]%2].append(i)

if len(node_list[0]) > len(node_list[1]):
    print(*node_list[0][:n//2])
else:
    print(*node_list[1][:n//2])



