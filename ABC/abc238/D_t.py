from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

def ok(a, s):
    if a * 2 > s:
        return False
    a = list(f'{bin(a)[2:]:0>61}')[::-1]
    s = list(f'{bin(s)[2:]:0>61}')[::-1]
    kuriagari = 0
    for i in range(61):
        s_tmp = int(s[i])
        a_tmp = int(a[i])
        flag = False
        if a_tmp == 1:
            if kuriagari:
                kuriagari = 1
                if s_tmp == 0:
                    flag = True
            else:
                kuriagari = 1
                if s_tmp == 1:
                    flag = True
        else:
            if kuriagari:
                if s_tmp == 0:
                    kuriagari = 1
                else:
                    kuriagari = 0
            else:
                if s_tmp == 0:
                    kuriagari = 0
                else:
                    kuriagari = 0
                
        if flag:
            return False
    return True

                     
            
t = ii()
for _ in range(t):
    a, s = mi()
    if ok(a, s):
        print('Yes')
    else:
        print('No')
