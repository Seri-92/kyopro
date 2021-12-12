n = int(input())
lst = [list(input().split()) for _ in range(n)]
T = []
for i in range(n):
    T.append(int(lst[i][1]))
T.sort()
t_max = str(T[-2])
for i in range(n):
    if lst[i][1] == t_max:
        print(lst[i][0])
    