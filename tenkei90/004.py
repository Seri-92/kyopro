import numpy as np
h, w = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(h)])
row = [sum(A[i, :]) for i in range(h)]
column = [sum(A[:, i]) for i in range(w)]
for i in range(h):
    for j in range(w):
        print(row[i] + column[j] - A[i, j])
