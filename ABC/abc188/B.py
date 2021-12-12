n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
naiseki = 0
for i in range(n):
    naiseki += A[i] * B[i]
print('Yes' if naiseki == 0 else 'No')
