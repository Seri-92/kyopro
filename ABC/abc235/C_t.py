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

n, q = mi()
A = lmi()
dict_ = dict()
for i in range(n):
    a = A[i]
    if a not in dict_:
        dict_[a] = [i]
    else:
        dict_[a].append(i)


for i in range(q):
    x, k = mi()
    if x not in dict_:
        print(-1)
    elif len(dict_[x]) < k:
        print(-1)
    else:
        print(dict_[x][k - 1] + 1)

