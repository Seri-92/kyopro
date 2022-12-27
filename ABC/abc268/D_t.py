from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

sys.setrecursionlimit(10**7)
# mod = 1000000007
# mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

n, m = mi()
S = [input() for _ in range(n)]

T = set(input() for _ in range(m))

def dfs(idx, s):
    if idx == n:
        if 3 <= len(s) <= 16:
            if s not in T and s[-1] != '_':
                print(s)
                exit()
        return
    else:
        if len(s) > 16 - len(l[idx]):
            return
        dfs(idx, s+'_')
        if idx == n - 1:
            s += l[idx]
            idx += 1
            dfs(idx, s)
        else:
            s += l[idx] + '_'
            idx += 1
            dfs(idx, s)


for l in permutations(S):
    if n == 1:
        dfs(1, l[0])
    else:
        dfs(1, l[0]+'_')

print(-1)


    
    
