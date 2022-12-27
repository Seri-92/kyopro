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

n, m = mi()
A = lmi()
B = lmi()
dict_ = {}
for a in A:
    if a not in dict_:
        dict_[a] = 1
    else:
        dict_[a] += 1

for b in B:
    if b in dict_ and dict_[b] > 0:
        dict_[b] -= 1
    else:
        print('No')
        exit()
print('Yes')

