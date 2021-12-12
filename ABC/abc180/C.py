n = int(input())

x = 1
ans = []
while x*x <= n:
    if n % x == 0:
        if x == n/x:
            ans.append(x)
        else:
        ans.append(x)
        ans.append(n//x)
    x +=1

ans.sort()
for i in range(len(ans)):
    print(ans[i])