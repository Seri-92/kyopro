h, w, n = map(int, input().split())
C = []
D = []
for i in range(n):
    c, d = map(int, input().split())
    C.append((c, i))
    D.append((d, i))
C.sort()
D.sort()
A = [(C[0][1], 1)]
B = [(D[0][1], 1)]
r_cnt = 1
c_cnt = 1
for i in range(1, n):
    if C[i][0] != C[i-1][0]:
        r_cnt += 1
    if D[i][0] != D[i-1][0]:
        c_cnt += 1
    A.append((C[i][1], r_cnt))
    B.append((D[i][1], c_cnt))
A.sort()
B.sort()
for i in range(n):
    print(A[i][1], B[i][1])





