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

n = ii()
s_list = [li() for _ in range(n)]
bingo_num = [-1] * n

ans = 1e10
for i in range(10):
    for j in range(n):
        for k in range(10):
            if s_list[j][k] == i:
                bingo_num[j] = k
    ans_tmp = -1
    for j in range(10):
        cnt = 0
        for x in bingo_num:
            if x == j:
                cnt += 1
        ans_tmp = max(ans_tmp, (cnt - 1) * 10 + j)
    ans = min(ans, ans_tmp)

print(ans)
