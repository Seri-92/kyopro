n, m = map(int, input().split())
h = list(map(int, input().split()))
false_set = set()
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if h[a] == h[b]:
        false_set.add(a)
        false_set.add(b)
    elif h[a] < h[b]:
        false_set.add(a)
    else:
        false_set.add(b)
print(n-len(false_set))