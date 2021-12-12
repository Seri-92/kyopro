n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
AA = [0] * n
for i in range(n):
    AA[A[i]-1] += 1


