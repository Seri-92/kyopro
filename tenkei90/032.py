import itertools

inf = 10**8
n = int(input())
members = list(range(n))
A = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
ng_list = [set() for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    ng_list[x].add(y)
    ng_list[y].add(x)

def f(l):
    ans = 0
    for i in range(n):
        if i < n-1:
            if l[i] in ng_list[l[i+1]]:
                return inf
        ans += A[l[i]][i]
    return ans

ans = inf

for l in itertools.permutations(members):
    ans = min(ans, f(l))
        

if ans == inf:
    ans = -1
print(ans)




