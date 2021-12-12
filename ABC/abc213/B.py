n = int(input())
A = list(map(int, input().split()))
B = []
for i in range(n):
    B.append((A[i], i+1))
B.sort()
print(B[-2][1])

