from math import gcd
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n, m = map(int, input().split())
A = list(map(int, input().split()))
x = 1
divisors = set()
for i in range(n):
    divisors |= set(make_divisors(A[i]))

y = 1
for q in divisors:
    y *= q
ans = []
for i in range(1, m+1):
    if gcd(i, y) == 1:
        ans.append(i)
print(len(ans))        
for i in range(len(ans)):
    print(ans[i])
