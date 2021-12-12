h, w = map(int, input().split())
meiro = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if meiro[i][j] == 's':start = (i, j)
        elif meiro[i][j] == 'g':goal = (i, j)

seen = [[0] * w for _ in range(h)]
todo = [start]

while todo:
    now = todo.pop()
    seen[now[0]][now[1]] = 1
    if now == goal:
        print('Yes')
        exit()
    lst = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for i in range(4):
        x, y= (now[0] + lst[i][0], now[1] + lst[i][1])
        if not(0 <=  x < w and 0 <= y < h): continue
        if seen[x][y]:continue
        seen[x][y] = 1
        if meiro[x][y] in {'.', 'g'}:
            todo.append((x, y))

print('No')
            

        
  
