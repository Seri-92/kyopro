n = int(input())
ans = 10**12
i = 1
while i ** 2 < n:
    j, r = divmod(n, i)
    if r == 0:
        ans = min(ans, i+j-2)
    i += 1
print(ans)