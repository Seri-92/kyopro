n = int(input())
As = list(map(int, input().split()))
lst = [0]
for k in range(2, 1000):
    a = 0
    for i in range(n):
        if As[i] % k == 0:
            a += 1
    lst.append(a)
    
idx = lst.index(max(lst))
print(idx + 1)