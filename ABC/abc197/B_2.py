h, w, x, y = map(int, input().split())
S = [list(input()) for _ in range(h)]
x -= 1
y -= 1

cnt = 0
if S[x][y] == '.':
    cnt += 1

for s in reversed(S[x][:y]):
    if s == '#':
        break
    cnt += 1
for s in S[x][y+1:]:
    if s == '#':
        break
    cnt += 1


for i in reversed(range(x)):
    if S[i][y] == '#':
        break
    cnt += 1

for i in range(x+1, h):
    if S[i][y] == '#':
        break
    cnt += 1
print(cnt)
