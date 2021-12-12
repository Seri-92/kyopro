import numpy as np
n = int(input())
lst = list(range(1, 10))
# test
t = []
for i in range(n):
    t.append(np.random.choice(lst))




# t = list(map(int, input().split()))
t.sort(reverse=True)
t_sum = sum(t)

a = b = 0
for i in range(n):
    if a < b:
        a += t[i]
    else:
        b += t[i]
print(f't={t}')
print(max(a, b))

