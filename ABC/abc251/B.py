n, w = map(int, input().split())

A = list(map(int, input().split()))

good_nums = set()

for i in range(n):
    x = A[i]
    if x <= w:
        good_nums.add(x)

for i in range(n):
    for j in range(i+1, n):
        x = A[i] + A[j]
        if x <= w:
            good_nums.add(x)


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x = A[i] + A[j] + A[k]
            if x <= w:
                good_nums.add(x)

print(len(good_nums))
