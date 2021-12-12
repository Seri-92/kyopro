N = int(input())
lst = [0] * N
for d in range(1, N):
    for n in range(d, N, d):
        lst[n] += 1
ans = sum(lst)
print(ans)
