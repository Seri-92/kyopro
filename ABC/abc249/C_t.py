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

n, k = mi()
s_list = [ls() for _ in range(n)]

s_cnt = [dict() for _ in range(n)]

ans = 0
for i in range(1<<n):
    c_cnt = {}
    for j in range(n):
        if i >> j & 1:
            for c in s_list[j]:
                if c in c_cnt:
                    c_cnt[c] += 1
                else:
                    c_cnt[c] = 1
    k_num = 0
    for key in c_cnt:
        if c_cnt[key] == k:
            k_num += 1 
    ans = max(k_num, ans)

print(ans)
