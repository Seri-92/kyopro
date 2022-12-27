from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

# sys.setrecursionlimit(10**7)
# mod = 1000000007
# mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))




n, x, y = mi()
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = mi()
    tree[u].append(v)
    tree[v].append(u)

inf = 1e8

dist = [inf] * (n+1)
dist[x] = 0
todo = deque()
todo.append(x)

while todo:
    v = todo.popleft()
    for w in tree[v]:
        if dist[w] == inf:
            dist[w] = dist[v] + 1
            todo.append(w)
        

ans = [y]
crr = y
while crr != x:
    for v in tree[crr]:
        if dist[v] == dist[crr] - 1:
            ans.append(v)
            crr = v
            break

print(*ans[::-1])
                    



    
    

    
