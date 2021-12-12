n = int(input())
P = list(map(int, input().split()))
Q = [0] * n
for i in range(n):
    Q[P[i]-1] = str(i+1)

print(' '.join(Q))
