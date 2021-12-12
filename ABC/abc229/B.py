a, b = input().split()
a = a[::-1]
b = b[::-1]

l = min(len(a), len(b))
for i in range(l):
    p, q = a[i], b[i]
    p = int(p)
    q = int(q)
    if p + q > 9:
        print('Hard')
        exit()
print('Easy')
        