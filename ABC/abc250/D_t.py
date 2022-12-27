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

def list_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range (0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, limit + 1, p):
            is_prime[i] = False

    return primes

prime_nums = list_primes(10**6)
ans = 0

l = len(prime_nums)

for i, p in enumerate(prime_nums):
    q_min = prime_nums[i+1]
    if p * q_min ** 3 > n:
        break
    q_max = prime_nums[-1]
    if p * q_max ** 3 <= n:
        ans += l - i
        continue
    idx_ng = l - 1
    idx_ok = i + 1
    while idx_ng - idx_ok > 1:
        mid = (idx_ng + idx_ok) // 2
        if p * prime_nums[mid] ** 3 <= n:
            idx_ok = mid
        else:
            idx_ng = mid
    ans += idx_ok - i

print(ans)

