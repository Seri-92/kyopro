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

n, k, q = mi()
A = lmi()
L = lmi()
board = [0] * (n + 1)
for i in range(k):
    board[A[i]] = 1
for i in range(q):
    l = L[i]
    cnt = 0
    for j in range(1, n+1):
        if board[j]:
            cnt += 1
        if cnt == l:
            break
    if j == n:
        continue
    if board[j+1]:
        continue
    board[j] = 0
    board[j+1] = 1

ans = []
for i in range(1, n+1):
    if board[i]:
        ans.append(i)

print(*ans)
