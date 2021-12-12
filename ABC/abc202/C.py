n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split())) 
AA = [0]*n
ans = 0
for i in range(n):
    AA[A[i]-1] += 1
# BB = [[] for _ in range(n)]
# for i in range(n):
#     BB[B[i]-1].append(i)
# CC = [0]*n
# for i in range(n):
#     CC[C[i]-1] += 1
# CC2 = [0]*n
BB = [0]*n
for i in range(n):
    BB[B[C[i]-1]-1] += 1

for i in range(n):
    ans += AA[i] * BB[i]
print(ans)
    

