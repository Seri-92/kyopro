import numpy as np
h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

A = np.array(A, dtype=int)
A_t = A.T
for i in range(w):
    print(*A_t[i])
    
