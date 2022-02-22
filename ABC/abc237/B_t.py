from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

h, w = mi()

A = [lmi() for _ in range(h)]

B = [[0] * h for _ in range(w)]

for i in range(w):
    for j in range(h):
        B[i][j] = A[j][i]

for i in range(w):
    print(*B[i])
