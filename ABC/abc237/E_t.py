from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

n, m = mi()
H = [0] + lmi()

G = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = mi()
    G[u].append(v)
    G[v].append(u)

def dfs(crr):
    visited[crr] = 1
    for nxt in G[crr]:
        if not visited[nxt]:
            visited[nxt] = 1
            if H[crr] >= H[nxt]:
                d_ureshisa = H[crr] - H[nxt]
            else:
                d_ureshisa = 2 * (H[crr] - H[nxt])
            ureshisa[nxt] = ureshisa[crr] + d_ureshisa
            dfs(nxt)
    
visited = [0] * (n + 1)
ureshisa = [0] * (n + 1)
dfs(1)
print(ureshisa)
    
