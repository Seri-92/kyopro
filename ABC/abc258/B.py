n = int(input())
A = [list(map(int, list(input()))) for _ in range(n)]
l = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
ans = 0
for i in range(n):
    for j in range(n):
        for dr, dc in l:
            route = [str(A[i][j])]
            for k in range(1, n):
                route.append(str(A[(i+dr*k)%n][(j+dc*k)%n]))
            ans = max(ans, int(''.join(route)))

print(ans)
