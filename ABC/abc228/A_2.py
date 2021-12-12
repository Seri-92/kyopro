s, t, x = map(int, input().split())
if s < t:
    if s <= x < t:
        ans = 'Yes'
    else:
        ans = 'No'
else:
    if s <= x or x < t:
        ans = 'Yes'
    else:
        ans = 'No'
print(ans)
