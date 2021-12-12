q = int(input())
n = 1048576
A = [-1] * n
B = [-1] * n

for _ in range(q):
    t, x = map(int, input().split())
    x_ind = x % n
    if t == 2:
        print(A[x_ind])
    else:
        if A[x_ind] == -1:
            A[x_ind] = x
            if x_ind == 0:
                B[x_ind] = x_ind
            else:
                if A[x_ind - 1] != -1:
                    B[x_ind] = B[x_ind - 1]
                else:
                    B[x_ind] = x_ind
            if x_ind == n - 1:
                continue
            else:
                if B[x_ind + 1] != -1:
                    B[x_ind + 1] = B[x_ind]
            C = 
            