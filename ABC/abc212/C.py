from bisect import bisect_left
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
banpei = 10 ** 10
B += [banpei, - banpei]
B.sort()
ans = 10 ** 10
for i in range(n):
    a = A[i]
    idx = bisect_left(B, a)
    ans = min(ans, abs(a-B[idx-1]), abs(a-B[idx]))
print(ans)