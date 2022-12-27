from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

# sys.setrecursionlimit(10**7)
# mod = 1000000007
mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

def count(n, s):
    l = 0--n//2
    ret = 0
    for i in range(l):
        c_tmp = s[i]
        x = ord(c_tmp) - 65
        if i == l-1:
            if n % 2 == 0:
                if s[:l] + s[:l][::-1] <= s:
                    # print(s[:l] + s[:l][::-1])
                    ret += x + 1
                else: ret += x
            else:
                if s[:l] + s[:l-1][::-1]<= s:
                    # print(s[:l] + s[:l-1][::-1])
                    ret += x + 1
                else: ret += x
            
        else:
            ret += (x * 26 ** (l - i - 1)) % mod
                 
    return ret % mod


t = ii()
for _ in range(t):
    n = ii()
    s = input()
    print(count(n, s))
