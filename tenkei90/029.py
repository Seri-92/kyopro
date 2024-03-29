w, n = map(int, input().split())
brick_list = [list(map(int, input().split())) for _ in range(n)]


N = w # N: 処理する区間の長さ
INF = 2**31-1

LV = (N-1).bit_length()
N0 = 2**LV
data = [0]*(2*N0)
lazy = [None]*(2*N0)
 
# 伝搬対象の区間を求める
def gindex(l, r):
    L = (l + N0) >> 1; R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1; R >>= 1
 
# 遅延伝搬処理
def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if v is None:
            continue
        lazy[2*i-1] = data[2*i-1] = lazy[2*i] = data[2*i] = v
        lazy[i-1] = None
 
# 区間[l, r)をxで更新
def update(l, r, x):
    *ids, = gindex(l, r)
    propagates(*ids)
 
    L = N0 + l; R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R-1] = data[R-1] = x
        if L & 1:
            lazy[L-1] = data[L-1] = x
            L += 1
        L >>= 1; R >>= 1
    for i in ids:
        data[i-1] = max(data[2*i-1], data[2*i])
 
# 区間[l, r)内の最大値を求める
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r
 
    s = 0
    while L < R:
        if R & 1:
            R -= 1
            s = max(s, data[R-1])
        if L & 1:
            s = max(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s
for i in range(n):
    l, r = brick_list[i]
    h_tmp = query(l-1, r) + 1
    print(h_tmp)
    update(l-1, r, h_tmp)

