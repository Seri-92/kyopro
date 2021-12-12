N = int(input())
T = list(map(int, input().split()))
M = int(input())
ans = []
for i in range(M):
    P, X = map(int, input().split())
    ans.append(sum(T) - T[P-1] + X)
print(*ans, sep="\n")