n, x = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in range(n):
    if A[i] != x:
        B.append(A[i])
print(' '.join(str(b) for b in B))