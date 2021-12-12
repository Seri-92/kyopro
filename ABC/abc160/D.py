# = map(int, input().split())
# = list(map(int, input().split()))
n, x, y = map(int, input().split())
x -= 1
y -= 1
ans = [0] * n
for i in range(n):
    for j in range(i+1, n):
        dist = min([j-i, abs(x-i)+abs(y-j)+1, abs(y-i)+abs(x-j)+1]) 
        ans[dist] += 1
for k in range(1, n):
    print(ans[k])
#"\n".join(ans)

#for k in range(1, n):
 #   finalans=ans.count(str(k))
 #   print(finalans)
