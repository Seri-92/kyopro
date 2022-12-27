n, q = map(int, input().split())
A = list(map(int, input().split()))
query_list = [list(map(int, input().split())) for _ in range(q)]

shift_cnt = 0

for query in query_list:
    if query[0] == 2:
        shift_cnt += 1
    elif query[0] == 1:
        i, j = query[1:]
        i = (i - shift_cnt - 1) % n
        j = (j - shift_cnt - 1) % n
        A[i], A[j] = A[j], A[i]
    else:
        i = query[1] - 1
        print(A[(i-shift_cnt) % n])
