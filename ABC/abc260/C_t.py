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

n, x, y = mi()

red_num = 1
blue_num = 0

for i in range(n-1):
    red_num_tmp = red_num * (x+1) + blue_num
    blue_num_tmp = red_num * (x*y) + blue_num * y

    # red_num_tmp *= blue_num
    # blue_num_tmp *= bulue_num * y
    red_num = red_num_tmp
    blue_num = blue_num_tmp

print(blue_num)
