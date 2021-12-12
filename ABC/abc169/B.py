n = int(input())
As = list(map(int, input().split()))
list(map(int, input().split()))
ans = 1
if 0 in As:
    print(0)
    exit()
for i in range(n):
    ans *= As[i]
    if ans > 1e18:
        print(-1)
        exit()

print(ans)