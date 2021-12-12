n, m = map(int, input().split())
list_ = []
for _ in range(m):
    k = int(input())
    A = list(map(int, input().split()))
    list_.append((k, A))
seen = [0] * n

for i in range(m):
    seen[list_[i][1][0] - 1] += 1

for i in range(n):
    if seen[i] > 1:
        seen[i] -= 2
        seen[]

        

     