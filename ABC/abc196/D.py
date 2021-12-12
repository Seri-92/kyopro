import numpy as np
h, w, a, b = map(int, input().split())
set_ = set()
A = np.zeros((h, w))
for i in range(h):
    for j in range(w):
        if A[i, j] != 0:
            continue
        if 