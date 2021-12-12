x = input()
m = int(input())

if len(x) == 1:
    if int(x) <= m:
        print(1)
    else:
        print(0)
    exit()

x_lst = []
n = len(x)
for i in range(n):
    x_lst.append(int(x[i]))
x_lst.reverse()
d_0 = sorted(list(x))[-1]
d_0 = int(d_0)
top = 1e18 + 1
bottom = d_0

a = 0
for i in range(n):
    a += x_lst[i] * (bottom+1)**i
if m < a:
    print(0)
    exit()

while top - bottom > 1:
    mid = int((bottom + top) // 2)
    a = 0
    for i in range(n):
        a += x_lst[i] * mid**i
    if m < a:
        top = mid
    else:
        bottom = mid

print(bottom - d_0)