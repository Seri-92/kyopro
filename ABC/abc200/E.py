from math import factorial
from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

n, k = map(int, input().split())
cnt = 0
for i in range(2, 3*n):
    cnt += i * (i-1)
    if cnt > k * 2:
        break
    d = k - (cnt // 2)
a = bin(int(('0b' + '1' * 2 + '0' * (i-2)), 2) + d - 1)
a = a[2:]
print(a)
lst = []
for i in range(len(a)):
    if a[i] == '1':
        lst.append(i)

p = lst[0] + 1
q = lst[1] - lst[0] - 2 + 1
r = i + 1 - p - q + 1
print(p, q, r)