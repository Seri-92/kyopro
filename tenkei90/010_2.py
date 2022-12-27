n = int(input())
points_1 = [0]*n
points_2 = [0]*n

for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        points_1[i] = p
    else:
        points_2[i] = p


accumulate_1 = [0]
accumulate_2 = [0]
for i in range(n):
    accumulate_1.append(points_1[i] + accumulate_1[-1])
    accumulate_2.append(points_2[i] + accumulate_2[-1])

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(accumulate_1[r+1]-accumulate_1[l], accumulate_2[r+1]-accumulate_2[l])

