s, t, x = map(int, input().split())
if t == 0:
    t = 24
if s <= t:
    if s <= x < t:
        ans = True
    else:
        ans = False

else:
    if 0 <= x < t or s <= x < 24:
        ans = True
    else:
        ans = False
print('Yes' if ans == True else 'No')