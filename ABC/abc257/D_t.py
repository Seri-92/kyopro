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





n = ii()

jump_ramps = [lmi() for _ in range(n)]

def make_graph(x):
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if i == j:
                continue
            a, b, p_1 = jump_ramps[i]
            c, d, p_2 = jump_ramps[j]
            dist = abs(a - c) + abs(b - d)
            if p_1 * x >= dist:
                G[i].append(j)
            if p_2 * x >= dist:
                G[j].append(i)
    return G

def bfs(G, start):
    seen = [0] * n
    seen[start] = 1
    todo = [start]
    while todo:
        v = todo.pop()
        seen[v] = 1
        for w in G[v]:
            if seen[w]:
                continue
            else:
                seen[w] = 1
                todo.append(w)
    if sum(seen) == n:
        return True
    return False

ok = 10**10
ng = 0

G = make_graph(ng)
for i in range(n):
    if bfs(G, i):
        print(0)
        exit()

while ok - ng > 1:
    mid = (ok + ng) // 2
    G = make_graph(mid)
    flag = False
    for i in range(n):
        if bfs(G, i):
            flag = True
            break
    if flag:
        ok = mid
    else:
        ng = mid

print(ok)
