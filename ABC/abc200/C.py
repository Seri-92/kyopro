from math import factorial
n = int(input())
A = list(map(int, input().split()))
for i in range(n):
    A[i] %= 200
ans = 0
for i in range(200):
    cnt = 0
    for j in range(n):
        if A[j] == i:
            cnt += 1
    if cnt < 2:
        continue
    ans += factorial(cnt) // (factorial(2)*factorial(cnt-2))
print(ans)