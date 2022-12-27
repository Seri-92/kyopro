SEG_LEN = 1 << 18
seg = [0] * (SEG_LEN*2)
ans_list = []
def add(idx, v):
    idx += SEG_LEN
    seg[idx] += v
    while True:
        idx //= 2
        if idx == 0: return
        seg[idx] = seg[idx*2] + seg[idx*2+1]
    return

def get_sum(l, r):
    ans = 0
    l += SEG_LEN
    r += SEG_LEN
    while l < r:
        if l % 2 == 1:
            ans += seg[l]
            l += 1
        l //= 2

        if r % 2 == 1:
            ans += seg[r-1]
            r -= 1
        r //= 2
    return ans


n, q = map(int, input().split())
q_list = [list(map(int, input().split())) for _ in range(q)]
for i in range(q):
    com, x, y = q_list[i]
    if com == 0:
        add(x, y)
    else:
        print(get_sum(x, y+1))

