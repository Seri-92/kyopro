SEG_LEN = 1<<18
INI = (1<<31) - 1

seg = [(-1, INI)] * (SEG_LEN*2)

def update(l, r, x, i):
    l += SEG_LEN
    r += SEG_LEN
    while l < r:
        if l % 2 == 1:
            seg[l] = (i, x)
            l += 1
        l //= 2

        if r % 2 == 1:
            seg[r-1] = (i, x)
            r -= 1
        r //= 2


def find(idx):
    idx += SEG_LEN
    list_ = []
    while True:
        if idx == 0:
            break
        list_.append(seg[idx])
        idx //= 2
    list_.sort(reverse=True)

    return list_[0][1]

    
n, q = map(int, input().split())
query_list = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    query = query_list[i]
    if query[0] == 0:
        s, t, x = query[1:]
        update(s, t+1, x, i)
    else:
        idx = query[1]
        print(find(idx))


