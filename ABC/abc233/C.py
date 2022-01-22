from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(10**6)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

n, x = mi()
list_ = [lmi() for _ in range(n)]

L = list()
for i in range(n):
    L.append(list_[i][0])
ans = []
# print(f'{L=}')

def is_x(A):
    p = 1
    for i in range(n):
        p *= list_[i][A[i]+1]
    return p == x


def dfs(A):
    if len(A) == n:
        # print(f'{A=}')
        if is_x(A):
            ans.append(1)
            return
        else:
            return

    for v in range(L[len(A)]):
        A.append(v)
        # print(A)
        dfs(A)
        A.pop()

dfs([])
print(len(ans))
