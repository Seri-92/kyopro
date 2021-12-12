n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
ans = 0
for b in B:
    A_top = n - 1
    A_bottom = 0
    while A_top - A_bottom > 0:
        A_mid = (A_top + A_bottom) // 2
        if A[A_mid] >= b:
            A_top = A_mid
        else:
            A_bottom = A_mid
    C_top = n
    C_bottom = n
    while C_top - C_bottom > 1:
        C_mid = (C_top + C_bottom) // 2
        if C[C_mid] > b:
            C_top = C_mid
        else:
            C_bottom = C_mid

    ans += A_bottom + (n - C_top + 1)

print(ans)

             


