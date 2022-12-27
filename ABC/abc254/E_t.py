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
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = mi()
    graph[a].append(b)
    graph[b].append(a)

q = ii()
for _ in range(q):
    x, k = mi()
    seen = [0] * (n + 1)
    seen[x] = x
    todo = deque([x])
    cnt = 0
    while cnt < k:
        cnt += 1
        while todo:
            v = todo.popleft()
            for w in graph[v]:
                if not seen[w]:
                    todo.append(w)
                    seen[w] = w
    print(sum(seen))


