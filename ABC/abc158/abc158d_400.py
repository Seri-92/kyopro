s = input()
q_num = int(input())
head = []
tail = []
flip = 0
for i in range(q_num):
    q = tuple(input().split())
    if q[0] == '1':
        flip ^= 1
    else:
        f = int(q[1]) - 1
        c = q[2]
        if f ^ flip == 0:
            head.append(c)
        else:
            tail.append(c)
if flip:
    head, tail = tail, head
    s = s[::-1]
head = ''.join(head)
tail = ''.join(tail)
print(head[::-1] + s + tail)