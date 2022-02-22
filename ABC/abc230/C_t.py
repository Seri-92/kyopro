from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

# sys.setrecursionlimit(10**7)
# mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

N, A, B = mi()
P, Q, R, S = mi()

def check_migishita(i, j):
    if i - A != j - B:
        return 0
    k = i - A
    if max(1 - A, 1 - B) > k:
        return 0
    if k > min(N - A, N - B):
        return 0
    return 1


def check_hidarishita(i, j):
    if i - A != B - j:
        return 0
    k = i - A
    if max(1 - A, B - N) > k:
        return 0
    if k > min(N - A, B - 1):
        return 0
    return 1

ans = [['.'] * (S - R + 1) for _ in range(Q - P + 1)]

for i in range(P, Q + 1):
    for j in range(R, S + 1):
        if check_migishita(i, j) or check_hidarishita(i, j):
            ans[i - P][j - R] = '#'

for i in range(Q - P + 1):
    print(''.join(ans[i]))
