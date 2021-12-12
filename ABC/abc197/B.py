h, w, x, y = map(int, input().split())
x -= 1
y -= 1
A = [list(input().split()) for _ in range(h)]
start = A[x][y]

x_tmp = x
y_tmp = y 
while True:
    x_tmp -= 1
    if x_tmp < 0:
        break
    if A[x_tmp][y_tmp] == '.':
        ans += 1
    else:
        break

