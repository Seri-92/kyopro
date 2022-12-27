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


def ok(x):
    if max_board > x[0]:
        return True
    if max_board < x[0]:
        return False
    for r, c in dict_[x[0]]:
        for i in range(n-1):
            nxt_list = [
                    [(r+1)%n, c], [(r+1)%n, (c+1)%n], [(r+1)%n, (c-1)%n],
                    [(r-1)%n, c], [(r-1)%n, (c+1)%n], [(r-1)%n, (c-1)%N],
                    [r, (c+1)%n], [r, (c-1)%n]
                    ]
            flag = False
            for r_tmp, c_tmp in nxt_list:
                if board[r_tmp][c_tmp] >= x[i+1]:
                    flag = True
                    break
            if not flag: return False
        return 
n = ii()
board = [li() for _ in range(n)]
dict_ = defaultdict(list)
for i in range(n):
    for j in range(n):
        dict_[board[i][j]].append((i, j))

max_board = 0
for i in range(1, 10):
    if dict_[i]:
        max_board = max(max_board, i)


ok = int('1'*n)
ng = int('9'*n)
if ok(ng):
    print(ng)
    exit()
while True:

