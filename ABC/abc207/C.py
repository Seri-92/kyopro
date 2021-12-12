n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        ti = lst[i][0]
        li, ri = lst[i][1], lst[i][2]
        tj = lst[j][0]
        lj, rj = lst[j][1], lst[j][2]


        if ti == 1:
            if tj == 1:
                if lj <= ri and rj >= li:
                    ans += 1
            elif tj == 2:
                if lj <= ri and rj > li:
                    ans += 1
            elif tj == 3:
                if lj < ri and rj >= li:
                    ans += 1
            else:
                if lj < ri and rj > li:
                    ans += 1
        elif ti == 2:
            if tj == 1:
                if lj < ri and rj >= li:
                    ans += 1
            elif tj == 2:
                if lj < ri and rj > li:
                    ans += 1
            elif tj == 3:
                if lj < ri and rj >= li:
                    ans += 1
            else:
                if lj < ri and rj > li:
                    ans += 1
        elif ti == 3:
            if ti == 1:
                if lj <= ri and rj > li:
                    ans += 1
            elif tj == 2:
                if lj <= ri and rj > li:
                    ans += 1
            elif tj == 3:
                if lj < ri and rj > li:
                    ans += 1
            else:
                if lj < ri and rj > li:
                    ans += 1
        else:
            if lj < ri and rj > li:
                ans += 1
print(ans)
