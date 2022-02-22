from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

# sys.setrecursionlimit(10**7)
# mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

n = ii()
A = lmi()

if n == 1:
    print(1)
    exit()
ans = 1
print(ans)
top = A[0]
list_ = []
# top, renzoku
renzoku = 1
for i in range(1, n):
    ans += 1
    if A[i] == top:
        renzoku += 1    
        if renzoku == top:
            ans -= top
            if ans != 0:
                top, renzoku = list_.pop()
            else:
                top = 0
                renzoku = 0
    else:
        if top != 0:
            list_.append([top, renzoku])
        renzoku = 1
        top = A[i]
    
    print(ans)

# dp = [[0]*3 for _ in range(n)]
# # top, renzoku, ans
# dp[0] = [A[0], 1, 1]
# for i in range(1, n):
#     if dp[i-1][0] == A[i]:
#         if dp[i-1][1] + 1 == dp[i-1][0]:
#             kkk
