h, w = map(int, input().split())
C = [list(input()) for _ in range(h)]
todo = []
for i in range(h):
    for j in range(w):
        if C[i][j] == '.':
            todo.append((i, j))
            
for _ in range(len(todo)):
    a, b = todo.pop()
    color_done = []
    if a > 0:
        color_done.append(C[a-1][b])
    if b > 0:
        color_done.append(C[a][b-1])
    if a < h - 1:
        color_done.append(C[a+1][b])
    if b < w - 1:
        color_done.append(C[a][b+1])

    list_ = list({'1', '2', '3', '4', '5'} - set(color_done))
    C[a][b] = str(list_[0])

for i in range(h):
    print(''.join(C[i]))