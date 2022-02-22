n = int(input())
A = set(map(int, input().split()))

ans = len(A) * (len(A) - 1) // 2
print(ans)
