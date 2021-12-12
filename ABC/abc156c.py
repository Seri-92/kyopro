N = int(input())
X = list(map(int, input().split()))
a = 0
for i in range(N):
    a += X[i]
a /= N
a += 0.5
a = int(a)
ans = 0
for j in range(N):
    ans += (X[j]-a)**2
print(ans)
    
    
