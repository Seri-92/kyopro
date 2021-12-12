a, b, x, y = map(int, input().split())
ans = x
if a <= b:
    if 2 * x < y:
        ans += 2 * x * (b-a) 
    else:
        ans += y * (b-a)
else:
    if 2 * x < y:
        ans += 2 * x * (a - b -1)
    else:
        ans += y * (a - b - 1)
    
print(ans)