n, m = map(int, input().split())
A = list(map(int, input().split())) 
ans = sum(A)

if ans > n:
    ans = -1
else:
    ans = n - ans

print(ans)