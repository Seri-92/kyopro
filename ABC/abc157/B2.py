a = []
for i in range(3):
    a += list(map(int, input().split()))
bg = [False]*9
n = int(input())
for i in range(n):
    b = int(input())
    if b in a:
        bg[a.index(b)] = True

num = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
for x, y, z in num:
    if bg[x] and bg[y] and bg[z]:
        print('Yes')
        exit()
print('No')

