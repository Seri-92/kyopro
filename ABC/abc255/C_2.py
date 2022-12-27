x, a, d, n = map(int, input().split())
if d == 0:
    print(abs(x - a))
    exit()

if d < 0:
    a = a + d * (n - 1)
    d = -d 

top = n - 1
bottom = 0

while top - bottom > 1:
    mid = (top + bottom) // 2
    y = a + d * mid
    if x < y:
        top = mid
    else:
        bottom = mid

ans = min(abs(x - a - d * top), abs(x - a - d * bottom))
print(ans)

