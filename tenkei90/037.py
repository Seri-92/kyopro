w, n = map(int, input().split())
spice_list = [0] + [list(map(int, input().split())) for _ in range(n)]

SEG_LEN = 1<<15
dp = [[-1] * (SEG_LEN*2) for _ in range(n+1)]


def find_max(i, l, r):
    l += SEG_LEN
    r += SEG_LEN
    ret = dp[i-1][l]
    while l < r:
        if l % 2 == 1:
            ret = max(ret, dp[i-1][l])
            # print(dp[-1][l])
            l += 1
        l //= 2

        if r % 2 == 1:
            ret = max(ret, dp[i-1][r-1])
            # print(dp[i-1][r-1])
            r -= 1
        r //= 2
    return ret

def update(i, idx, v):
    idx += SEG_LEN
    dp[i][idx] = v
    while True:
        idx //= 2
        if idx == 0:
            break
        dp[i][idx] = max(dp[i][idx*2], dp[i][idx*2+1])

update(0, 0, 0)



for i in range(1, n+1):
    l, r, v = spice_list[i]
    for j in range(w+1):
        dp[i][j+SEG_LEN] = dp[i-1][j+SEG_LEN]

        if j < l: continue
        x = find_max(i, max(0, j-r), j-l+1)
        # print(f'{i=}|{j=}|{x=}')
        if x < 0:
            continue
            
        update(i, j, max(dp[i][j+SEG_LEN], x + v))
        

print(dp[n][w+SEG_LEN])
# print(dp[0][SEG_LEN:SEG_LEN+20])
# print(dp[1][SEG_LEN:SEG_LEN+20])
# print(dp[2][SEG_LEN:SEG_LEN+20])
