h, w, n = map(int, input().split())

field = [[0] * w for _ in range(h)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    field[a][b] += 1
    if d < w - 1:
        field[a][d+1] -= 1
    if c < h - 1:
        field[c+1][b] -= 1
    if c < h - 1 and d < w - 1:
        field[c+1][d+1] += 1

for i in range(h):
    for j in range(w-1):
        field[i][j+1] += field[i][j]

for i in range(h-1):
    for j in range(w):
        field[i+1][j] += field[i][j]

for i in range(h):
    print(*field[i])
