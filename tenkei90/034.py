from collections import defaultdict
n, k = map(int, input().split())
A = list(map(int, input().split()))

enumerate_num = defaultdict(int)
enumerate_num[A[0]] += 1

i = j = 0
cnt = 1
ans = 0

while True:
    j += 1
    if j > n-1:
        break
    enumerate_num[A[j]] += 1
    if enumerate_num[A[j]] == 1:
        cnt += 1
        

    if cnt > k:
        ans = max(ans, j-i)
        j -= 1
        enumerate_num[A[j+1]] -= 1
        cnt -= 1
        i += 1
        if i > n-1:
            break
        enumerate_num[A[i-1]] -= 1
        if enumerate_num[A[i-1]] == 0:
            cnt -= 1
    else:
        ans = max(ans, j-i+1)


print(ans)

