n, k = map(int, input().split())

def sum_count(x):
    return (2*n-x+1)*x//2 - x*(x-1)//2 + 1

ans = 0 
for i in range(k, n+2):
    ans += sum_count(i)
ans %= 10 ** 9 + 7

print(ans)