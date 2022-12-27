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

a = 0
square_set = set()
while a ** 2 <= m:
    square_set.add(a**2)
    a += 1

move_list = []
a = 0
while a ** 2 <= m // 2:
    if m - a ** 2 in square_set:
        b = int(math.sqrt(m - a ** 2))
        move_list.append((a, b))
    a += 1

    
board = [[-1] * n for _ in range(n)]
board[0][0] = 0
seen = [[0] * n for _ in range(n)]
seen[0][0] = 1
todo = deque([(0, 0)])
cnt = 1


def f(cnt, i, j, a, b):
    x, y = i - a, j - b
    if 0 <= x < n and 0 <= y < n:
        if not seen[x][y]:
            board[x][y] = cnt
            seen[x][y] = 1
            todo.append((x, y))
while todo:
    i, j = todo.popleft()
    cnt = board[i][j] + 1
    for a, b in move_list:
        f(cnt, i, j, a, b)
        f(cnt, i, j, -a, b)
        f(cnt, i, j, a, -b)
        f(cnt, i, j, -a, -b)
        f(cnt, i, j, b, a)
        f(cnt, i, j, -b, a)
        f(cnt, i, j, b, -a)
        f(cnt, i, j, -b, -a)


for i in range(n):
    print(*board[i])
