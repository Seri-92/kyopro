from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
import numpy as np

# sys.setrecursionlimit(10**7)
# mod = 1000000007
# mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

l = lmi()
H = l[:3]
W = l[3:]

def check_condition(i, j, k, l):
    board = np.zeros((3, 3), dtype=int)
    board[0, 0] = i
    board[0, 1] = j
    board[1, 0] = k
    board[1, 1] = l

    x = H[0] - sum(board[0, :])
    if x < 1:
        return False
    else:
        board[0, 2] = x

    x = H[1] - sum(board[1, :])
    if x < 1:
        return False
    else:
        board[1, 2] = x

    x = W[0] - sum(board[:, 0])
    if x < 1:
        return False
    else:
        board[2, 0] = x
    
    x = W[1] - sum(board[:, 1])
    if x < 1:
        return False
    else:
        board[2, 1] = x

    x = H[2] - sum(board[2, :])
    if x < 1:
        return False
    else:
        board[2, 2] = x

    if sum(board[:, 2]) != W[2]:
        return False
    
    # print(board)
    
    return True


    
ans = 0

for i in range(1, 29):
    for j in range(1, 29):
        for k in range(1, 29):
            for l in range(1, 29):
                if check_condition(i, j, k, l):
                    ans += 1

print(ans)
