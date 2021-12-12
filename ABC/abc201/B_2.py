n = int(input())
lst = []
for _ in range(n):
    s, t = input().split()
    t = int(t)
    lst.append((t, s))
lst.sort()
print(lst[-2][1])
