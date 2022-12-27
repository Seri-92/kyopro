def main():

    # input
    w, n = map(int, input().split())
    lrv = [0] + [list(map(int, input().split())) for _ in range(n)]

    seg = [-1] * (SEG_LEN*2)
    update(seg, 0, 0)
    for i in range(1, n+1):
        seg_tmp = seg[:]
        l, r, v = lrv[i]
        for j in range(l, w+1):
            max_ = find_max(seg, max(0, j-r), j-l+1)
            if max_ < 0:
                continue
            if max_ + v > get_val(seg_tmp, j):
                update(seg_tmp, j, max_ + v)

        seg = seg_tmp
        # print(seg[SEG_LEN:SEG_LEN+20])

    print(get_val(seg, w))
        
        


# find max value in [l, r)
def find_max(seg, l, r):
    l += SEG_LEN
    r += SEG_LEN
    ret = -1
    while l < r:
        if l & 1:
            ret = max(ret, seg[l])
            l += 1
        l >>= 1

        if r & 1:
            ret = max(ret, seg[r-1])
            r -= 1
        r >>= 1
    return ret

def get_val(seg, idx):
    return seg[idx+SEG_LEN]
    
# update seg[idx] as v
def update(seg, idx, v):
    idx += SEG_LEN
    seg[idx] = v
    while True:
        idx >>= 1
        if idx == 0:
            return
        seg[idx] = max(seg[idx*2], seg[idx*2+1])


SEG_LEN = 1 << 14

if __name__ == '__main__':
    main()
