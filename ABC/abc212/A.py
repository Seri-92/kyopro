a, b = map(int, input().split())
if a == 0 and b > 0:
    ans = 'Silver'
elif b == 0 and a > 0:
    ans = 'Gold'

else:
    ans = 'Alloy'
print(ans)
