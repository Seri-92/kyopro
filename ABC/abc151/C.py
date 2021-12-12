n, m = map(int, input().split())
lst = [[0, 0] for _ in range(n)]

for _ in range(m):
    p, s = input().split()
    p = int(p)
    if s == 'AC':
        lst[(p-1)][0] = 1
    elif lst[(p-1)][0] == 0:
        lst[(p-1)][1] += 1

correct = 0
wrong = 0
for i in range(n):
    correct += lst[i][0]
    if lst[i][0] == 1:
        wrong += lst[i][1]
        
print(correct, wrong)