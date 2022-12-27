n = int(input())
P = list(map(int, input().split()))

cnt = 0
min_tmp = n+1
for i in range(n):
    p_tmp = P[i]
    if min_tmp > p_tmp:
        cnt += 1
    min_tmp = min(min_tmp, p_tmp)

print(cnt)
