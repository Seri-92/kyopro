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

x_int = ii()
x = list(str(x_int))
l = len(x)
if l == 1:
    print(x_int)
    exit()
d_0 = int(x[0]) - int(x[1])
for k in range(2):
    for i in range(10):
        list_ = [str(int(x[0]) + k)]
        list_.append(str(i))
        d = int(list_[1]) - int(list_[0])
        for j in range(l-2):
            y = int(list_[-1]) + d
            if y > 9 or y < 0:
                break
            list_.append(str(y))
        if len(list_) == l:
            ans = int(''.join(list_))
            if ans >= x_int:
                print(ans)
                exit()

        
