x = int(input())
if x < 100:
    ans = 'No'
elif x % 100 != 0:
    ans = 'No'
else:
    ans = 'Yes'
print(ans)