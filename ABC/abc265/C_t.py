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

h, w = mi()
board = [ls() for _ in range(h)]
seen = [[0] * w for _ in range(h)]
x, y = 0, 0
seen[x][y] = 1

def seen_check_update(x, y):
    if seen[x][y]:
        print(-1)
        exit()
    seen[x][y] = 1
while True:
    if board[x][y] == 'U':
        if x < 1:
            break
        else:
            x -= 1
            seen_check_update(x, y)
    elif board[x][y] == 'D':
        if x >= h-1:
            break
        else:
            x += 1
            if seen[x][y]:
                print(-1)
                exit()
            seen[x][y] = 1
    elif board[x][y] == 'L':
        if y < 1:
            break
        else:
            y -= 1
            seen_check_update(x, y)
    else:
        if y >= w-1:
            break
        else:
            y += 1
            seen_check_update(x, y)
print(x+1, y+1)

