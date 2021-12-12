a, b, w = map(int, input().split())
w *= 1000
m = 2e7
M = 0
for i in range(1, 10**6+1):
    if a * i <= w <= b * i:
        m = min(m, i)
        M = max(M, i)

if M == 0:
    print('UNSATISFIABLE')
else:
    print(m, M)