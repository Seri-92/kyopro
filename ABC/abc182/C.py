n = list(input())
k = len(n)
ans = k
for i in range(2**k):
    switchs = [0] * (k+1)
    for j in range(1, k+1):
        switchs[j] = i >> (j-1) & 1
    num = 0
    for l in range(k):
        num += int(n[l]) * switchs[l+1]
    if num %3 == 0:
        ans = min(ans, switchs.count(0)-1)
if ans == k:
    ans = -1
print(ans)