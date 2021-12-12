n, k, m = map(int, input().split())
a = list(map(int, input().split()))
a = sum(a)
for i in range(k+1):
    if a + i >= m * n:
        print(i)
        exit()
print(-1)