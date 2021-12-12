h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
flag = True
for i in range(h-1):
    for ii in range(i+1, h):
        for j in range(w-1):
            for jj in range(j+1, w):
                if A[i][j] + A[ii][jj] > A[i][jj] + A[ii][j]:
                    flag = False

print('Yes' if flag else 'No')
