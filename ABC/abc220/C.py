n = int(input())
A = list(map(int, input().split()))
x = int(input())

b = sum(A)
ans = x // b * n 
x %= b

for i in range(n):
    x -= A[i]
    if x < 0:
        ans += i + 1
        break

print(ans)
