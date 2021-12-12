n = int(input())
A = list(map(int, input().split()))

A_sum = 0
for a in A:
    A_sum += a

ans = 0
for a in A:
    ans += a**2 * (n-1) - a * (A_sum - a)

print(ans)