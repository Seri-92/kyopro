a, b, x = map(int, input().split())
if a + b > x:
    print(0)
    exit()
ok = 1
ng = 10 **  9 + 1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if a * mid + b * len(str(mid)) <= x:
        ok = mid
    else:
        ng = mid

print(ok)
