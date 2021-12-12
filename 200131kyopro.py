n, a, b = map(int, input().split())
ans=0
for i in range(n+1):
    if a <= sum([int(x) for x in str(i)])<= b:
        ans+=i
print(ans)