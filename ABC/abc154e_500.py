W, H, N = map(int, input().split())
x_l, x_r, y_l, y_r = 0, W, 0, H
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        x_l = max(x_l, x)
    elif a == 2:
        x_r = min(x_r, x)
    elif a ==3:
        y_l = max(y_l, y)
    else:
        y_r = min(y_r, y)
if x_l >= x_r or y_l >= y_r:
    print(0)
    exit()
print((x_r-x_l)*(y_r-y_l))
