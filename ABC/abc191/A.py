v, t, s, d = map(int, input().split())
if v * t <= d <= v * s:
    ans = 'No'
else:
    ans = 'Yes'

print(ans)