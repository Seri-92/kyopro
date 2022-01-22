n = int(input())
A = list(map(int, input().split()))
A.sort()
print(A)
min_sum = A[-1] + A[-2]
max_sum = A[0] + A[1]

for i in range(n):
    x = A[i]
    y = A[2*n-i-1]
    min_sum = min(x + y, min_sum)
    max_sum = max(x + y, max_sum)

print(max_sum - min_sum)
