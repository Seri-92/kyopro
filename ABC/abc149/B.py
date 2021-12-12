a, b, k = map(int, input().split())
if k <= a:
    a1 = a - k
    b1 = b
elif a < k and k < a + b:
    a1 = 0
    b1 = b - (k-a)
else:
    a1 = 0
    b1 = 0

print(a1, b1)