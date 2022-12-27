l = list(range(777, 0, -1))

ans = 1
load_tmp = 0
for x in l:
    if load_tmp <= 5000 - x:
        load_tmp += x
    else:
        ans += 1
        load_tmp = x

print(ans)
