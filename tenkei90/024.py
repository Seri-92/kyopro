n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(n):
    cnt += abs(A[i] - B[i])

if cnt > k:
    print('No')
    exit()

if (k - cnt) % 2 == 0:
    print('Yes')
else:
    print('No')
