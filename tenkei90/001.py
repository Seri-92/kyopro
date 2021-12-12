n, l = map(int, input().split())
k = int(input())
A = [0] + list(map(int, input().split()))

def is_ok(sum_list_, k, x):
    l_tmp = 0
    start = 0
    stop = 0
    len_tmp = sum_list_[stop] - sum_list_[start] 
    for num in range(k):
        flag = 0
        for i in range(1, n+1):
            stop = start + i
            if stop > n:
                flag = 1
                break
            len_tmp = sum_list_[stop] - sum_list_[start]
            if len_tmp >= x:
                break

        if flag: return False
        start = stop
    if l - sum_list_[stop] >= x:
        return True
    return False

    
ok = 0
ng = l

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(A, k, mid):
        ok = mid
    else:
        ng = mid
print(ok)
