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
def li(): return list(input())

n, k, x, y = mi()
A = lmi()


heal_num = []
for i in range(n):
    num_tmp = 0 - -(A[i] - 1) // k
    if num_tmp > 0:
        heal_num.append(num_tmp)

heal_num.sort(reverse=True)
l = len(heal_num)
if l == 0:
    print(0)
    exit()

# print(f'{heal_num=}')

behoma_bound = y // x 
# print(f'{behoma_bound=}')
if behoma_bound <= 0:
    behomara_num = heal_num[0]
elif behoma_bound > l:
    behomara_num = 0
else:
    behomara_num = heal_num[behoma_bound]
# print(f'{behomara_num=}')
ans = y * behomara_num
for i in range(l):
    ans += max(0, (heal_num[i] - behomara_num) * x)

print(ans)
