from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

# sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

n, m = mi()
G = [[] for _ in range(n+1)]
for i in range(m):
    a, b = mi()
    G[a].append(b)
    G[b].append(a)
dist = [-1] * (n + 1)
dist[1] = 0
todo = deque()
todo.append(1)
cnt = [0] * (n + 1)
cnt[1] = 1

while todo:
    v = todo.popleft()
    for vv in G[v]:
        if dist[vv] < 0:
            todo.append(vv)
            dist[vv] = dist[v] + 1
            cnt[vv] += cnt[v]
            cnt[vv] %= mod
        else:
            if dist[vv] == dist[v] + 1:
                cnt[vv] += cnt[v]
                cnt[vv] %= mod


print(cnt[n])
# print(dist)
# print(f'{cnt=}')
    
