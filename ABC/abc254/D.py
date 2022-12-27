n = int(input())
square_nums = []
x = 1
while x ** 2 <= n:
    square_nums.append(x ** 2)
    x += 1

cnt = 0
for i in range(1, n+1):
    remains = i
    for x2 in square_nums[::-1]:
        if remains % x2 == 0:
            remains = i // x2
            break
    cnt_tmp = 0
    t = 0
    while True:
        if t > len(square_nums) - 1:
            break
        y2 = square_nums[t]
        j = remains * y2
        if j <= n:
            cnt_tmp += 1
            t += 1
        else:
            break
    cnt += cnt_tmp

print(cnt)
