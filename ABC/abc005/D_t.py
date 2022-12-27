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
board = [[0] * (n+1)]
for _ in range(n):
    board.append([0] + lmi())

for i in range(n+1):
    for j in range(n):
        board[i][j+1] += board[i][j]

for j in range(n+1):
    for i in range(n):
        board[i+1][j] += board[i][j]


d_list = [0] * (n**2 + 1)
for r1 in range(n):
    for r2 in range(1, n+1):
        for c1 in range(n):
            for c2 in range(1, n+1):
                area = (r2-r1) * (c2-c1)
                d_tmp = board[r2][c2] - board[r1][c2] - board[r2][c1] + board[r1][c1]
                d_list[area] = max(d_list[area], d_tmp)

for i in range(n**2):
    d_list[i+1] = max(d_list[i], d_list[i+1])


                
q = ii()
ans_list = []
for _ in range(q):
    p = ii()
    ans_list.append(d_list[p])

for ans in ans_list:
    print(ans)

