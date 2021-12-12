import math
p = int(input())

lst = []
for i in range(10):
    lst.append(math.factorial(10-i))

ans = 0
r = p
for i in range(10):
    q, r = divmod(r, lst[i])
    ans += q

print(ans)
