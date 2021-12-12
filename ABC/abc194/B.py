n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 1e6
for i in range(n):
    for j in range(n):
        if i == j:
            ans = min(ans, A[i]+B[j])
        else:
            ans = min(ans, max(A[i], B[j]))

print(ans)