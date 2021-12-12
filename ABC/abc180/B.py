n = int(input())
X = list(map(int, input().split()))
for i in range(n):
    X[i] = abs(X[i])

print(sum(X))

ans_2 = 0
for i in range(n):
    ans_2 += X[i] ** 2
ans_2 = ans_2 ** (1/2)
print(ans_2)

print(max(X))