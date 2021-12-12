k = int(input())
a, b = input().split()
a = a[::-1]
b = b[::-1]
p = 0
q = 0
for i in range(len(a)):
    p += int(a[i]) * k**i 

for i in range(len(b)):
    q += int(b[i]) * k**i
print(p * q)