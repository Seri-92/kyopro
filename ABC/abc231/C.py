n, q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = []
for _ in range(q):
    x = int(input())
    if A[-1] < x:
        ans.append(0)
        continue
    ok = n - 1
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if A[mid] >= x:
            ok = mid
        else:
            ng = mid
    ans.append(n-ok)

for i in range(q):
    print(ans[i])