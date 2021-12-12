n, k = map(int, input().split())
Hs = list(map(int, input().split()))
ans = 0 

for i in range(n):
    if Hs[i] >= k:
        ans += 1
        
print(ans) 