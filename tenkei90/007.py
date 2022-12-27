from bisect import bisect_left
n = int(input())
A = list(map(int, input().split()))
q = int(input())

A.sort()
l = len(A)
for _ in range(q):
    b = int(input())
    idx = bisect_left(A, b)
    if idx == 0:
        r = abs(A[idx] - b)
    elif idx == l:
        r = abs(A[idx-1] - b)
    else:
        r = min(abs(A[idx] - b), abs(A[idx-1] - b))
    print(r)

