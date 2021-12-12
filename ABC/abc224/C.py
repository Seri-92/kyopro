n = int(input())
list_ = [list(map(int, input().split())) for _ in range(n)]

def icchoku(p, q, r):
    px, py = p
    qx, qy = q
    rx, ry = r
    qx -= px
    rx -= px
    qy -= py
    ry -= py

    if qx * ry == qy * rx:
        flag = 1
    else:flag = 0
    return flag
    

cnt = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            p = list_[i]
            q = list_[j]
            r = list_[k]
            if not icchoku(p, q, r):
                cnt += 1
print(cnt)

