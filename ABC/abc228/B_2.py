n, x = map(int, input().split())
A = [0] + list(map(int, input().split()))


set_ = set([x])
crr = x
while True:
    nxt = A[crr]
    if nxt in set_:
        break
    set_.add(nxt)
    crr = nxt

print(len(set_))
