# = map(int, input().split())
# = list(map(int, input().split()))
k, n = map(int, input().split())
a = list(map(int, input().split()))
b = [a[0]+k-a[n-1]]
for i in range(n-1):
    b.append(a[i+1]-a[i])
print(k-max(b))
