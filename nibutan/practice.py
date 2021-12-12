n, k = map(int, input().split())
A = list(map(int, input().split()))
if A[-1] < k:
    print(-1)
    exit()
top = len(A) - 1
bottom = 0

while top - bottom > 1:
    mid = (top + bottom) // 2
    if A[mid] >= k:
        top = mid
    else:
        bottom = mid
print(top)
