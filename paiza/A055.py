h, w = map(int, input().split())
G = []
for i in range(h):
    x = list(input())
    G.append(x)
    for j in range(w):
        if x[j] == 'S':
            s = (i, j)
seen = [[0] * w for _ in range(h)]
seen[s[0]][s[1]] = 1
todo = [[s[0], s[1]]]
while todo:
    crr_r, crr_c= todo.pop()
    if crr_r in [0, h-1] or crr_c in [0, w-1]:
        if G[crr_r][crr_c] != '#':
            print('YES')
            exit()
    if crr_r > 0:
        if not seen[crr_r-1][crr_c]:
            if G[crr_r-1][crr_c] != '#':
                todo.append([crr_r-1, crr_c])
            seen[crr_r-1][crr_c] = 1
    if crr_c > 0:
        if not seen[crr_r][crr_c-1]:
            if G[crr_r][crr_c-1] != '#':
                todo.append([crr_r, crr_c-1])
            seen[crr_r][crr_c-1] = 1
    if crr_r < h - 1:
        if not seen[crr_r+1][crr_c]:
            if G[crr_r+1][crr_c] != '#':
                todo.append([crr_r+1, crr_c])
            seen[crr_r+1][crr_c] = 1
    if crr_c < w - 1:
        if not seen[crr_r][crr_c+1]:
            if G[crr_r][crr_c+1] != '#':
                todo.append([crr_r, crr_c+1])
print('NO')
