n = int(input())
a = list(map(int, input().split()))
accum_sum = a[:]
for i in range(1, n):
    accum_sum[i] += accum_sum[i-1]

accum_max = accum_sum[:]
for i in range(1, n):
    accum_max[i] = max(accum_max[i-1], accum_max[i])
now = 0
ans = 0
for i in range(n):
    ans = max(ans, now + accum_max[i])
    now += accum_sum[i]

print(ans)