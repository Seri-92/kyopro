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
            t.appendleft(s[i])
        else:
            t.append(s[i])
t = list(t)
if len(t) == 0:
    print('')
    exit()
if flip:
    t = t[::-1]
if len(t) == 1:
    print(t[0])
    exit()

ans = [t[0]]x
for i in range(1, len(t)):
    ans.append(t[i])
    if len(ans) < 2:
        continue
    if ans[-2] == ans[-1]:
        ans.pop()
        ans.pop()
print(''.join(ans))
