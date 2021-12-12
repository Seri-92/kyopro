n, x = map(int, input().split())
A = list(map(int, input().split()))
know = set([x])
p = x
while True:
    next = A[p-1]
    if next in know:
        break
    know.add(next)
    p = next
print(len(know))
   