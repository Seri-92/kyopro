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

n, a, b = mi()
all_sum = (1 + n) * n // 2
a_sum = (a + (n // a * a)) * (n // a) // 2
b_sum = (b + (n // b * b)) * (n // b) // 2
lcm = a * b // math.gcd(a, b)
ab_sum = (lcm + (n // lcm * lcm)) * (n // lcm) // 2

print(all_sum - a_sum - b_sum + ab_sum)
