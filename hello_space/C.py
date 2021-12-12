from collections import deque
s = input()
n = len(s)
t = deque()
flip = 0
for i in range(n):
    if s[i] == 'R':
        flip ^= 1
    else:
        if flip:
            t.appendleft[s[i]]
        else:
            t.append(s[i])
if flip:
    t = t[::-1]
