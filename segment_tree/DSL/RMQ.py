SEG_LEN = 1 << 18
INF = (1<<31) - 1
seg = [INF] * (SEG_LEN*2)

def update(idx, v):
    idx += SEG_LEN
    seg[idx] = v
    while True:
        idx //= 2
        if idx == 0:
            return
        seg[idx] = min(seg[idx*2], seg[idx*2+1])
    
def find_min(l, r):
    l += SEG_LEN
    r += SEG_LEN
    ret = INF

    while l < r:
        if l % 2 == 1:
            ret = min(ret, seg[l])
            l += 1
        l //= 2

        if r % 2 == 1:
            ret = min(ret, seg[r-1])
            r -= 1
        r //= 2
    return ret

n, q = map(int, input().split())
ans_list = []
for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        update(x, y)
    else:
        ans_list.append(find_min(x, y+1))

for ans in ans_list:
    print(ans)
