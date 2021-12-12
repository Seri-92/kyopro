n, k = map(int, input().split())
A = list(map(int, input().split()))
A_sorted = sorted(A)
q, r = divmod(k, n)
ans = [q] * n
if r > 0:
    x = A_sorted[r-1]
    for i in range(n):
        if A[i] <= x:
            ans[i] += 1

for i in range(n):
    print(ans[i])
