k = int(input())
a, b = map(int, input().split())
q = a // k
if q * k == a: 
    ans = 'OK'
elif (q+1) * k >= a and (q+1) * k <= b:
    ans = 'OK'
else:
    ans = 'NG'
print(ans)