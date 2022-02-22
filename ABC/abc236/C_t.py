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
 
n, m = mi()
S = list(input().split())
T = list(input().split())

i, j = 0, 0
while True:
    if T[j] == S[i]:
        print('Yes')
        i += 1
        j += 1
    else:
        print('No')
        i += 1
    if i == n:
        break


