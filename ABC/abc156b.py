N, K = map(int, input().split())
a = N
i = 0
while a >= 0:
    a = N - K ** i
    i += 1
print(i-1)