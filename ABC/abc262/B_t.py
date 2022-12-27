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

n, m = mi()
G = [set() for _ in range(n+1)]
for _ in range(m):
    u, v = mi()
    G[u].add(v)
    G[v].add(u)


ans = 0

for a in range(1, n+1):
    for b in range(a+1, n+1):
        for c in range(b+1, n+1):
            flag = True
            if not (b in G[a] and c in G[a]):
                flag = False
            if not (a in G[b] and c in G[b]):
                flag = False
            if flag:
                ans += 1

print(ans)
