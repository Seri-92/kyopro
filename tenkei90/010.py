n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

sum_data = [[0, 0] for _ in range (n+1)]
for i in range(n):
    if data[i][0] == 1:
        sum_data[i+1][0] = sum_data[i][0] + data[i][1]
        sum_data[i+1][1] = sum_data[i][1]
    else:
        sum_data[i+1][1] = sum_data[i][1] + data[i][1]
        sum_data[i+1][0] = sum_data[i][0]
print(data)
print(f'sum_data = {sum_data}')

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    a_0 = sum_data[r+1][0] - sum_data[l][0]
    a_1 = sum_data[r+1][1] - sum_data[l][1]
    print(a_0, a_1)
    




