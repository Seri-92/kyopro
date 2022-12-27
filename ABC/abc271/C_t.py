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
A = lmi()
A.sort()
B = [A[0]]
cnt = 0
for i in range(1, n):
    if A[i] == A[i-1]:
        cnt += 1
        continue
    else:
        B.append(A[i])


l = len(B)
i = 1
idx = 0
idx_end = l - 1
ans = 0
while idx <= idx_end:
    if B[idx] == i:
        i += 1
        ans += 1
        idx += 1
    else:
        if cnt >= 2:
            cnt -= 2
            i += 1
            ans += 1
        else:
            if cnt > 0:
                cnt -= 1
                idx_end -= 1
                i += 1
                ans += 1
            else:
                if idx_end > idx:
                    idx_end -= 2
                    i += 1
                    ans += 1
                else:
                    break
            
 
if cnt > 0:
    ans += cnt // 2

print(ans)
