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

seen = [[[0, 0] for _ in range(2020)] for _ in range(2020)]
black_set = set()
for _ in range(n):
    x, y = lmi()
    x += 1005
    y += 1005
    seen[x][y][0] = 1
    black_set.add(str(x) + '.' + str(y))
cnt = 0
next_d = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, 0], [1, 1]]
while black_set:
    todo = []
    r = black_set.pop()
    p, q = r.split('.')
    p = int(p)
    q = int(q)
    todo.append([p, q])
    seen[p][q][1] = 1
    while todo:
        x, y = todo.pop()
        for dx, dy in next_d:
            if seen[x+dx][y+dy] == [1, 0]:
                seen[x+dx][y+dy][1] = 1
                todo.append([x+dx, y+dy])
                black_set.remove(str(x+dx) + '.' + str(y+dy))
    cnt += 1 

print(cnt)



