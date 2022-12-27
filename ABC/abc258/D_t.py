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

n, x = mi()
stage = [lmi() for _ in range(n)]

# accumulate_min
accumulate_min = [1.1e18]

for i in range(n):
    accumulate_min.append(min(accumulate_min[-1], stage[i][1]))

# accumulate_first_time
accumulate_first_time = [0]
for i in range(n):
    accumulate_first_time.append(accumulate_first_time[-1]+sum(stage[i]))
# up to i_th stage
ans = 1.1e18
for i in range(n):
    if i > x:
        continue
    min_tmp = accumulate_first_time[i+1] + accumulate_min[i+1] * (x - i - 1)
    ans = min(ans, min_tmp)

    
print(ans)



