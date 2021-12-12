import sys
sys.setrecursionlimit(10 ** 9)

#n, m = map(int, input().split())

root = [-1] * 4

def r(x):
    if root[x] < 0:
        return x
    else:
        root[x] = r(root[x])
        return root[x]

def unite(x, y):
    x = r(x)
    y = r(y)
    if x == y:
        return
    root[x] += root[y]
    root[y] = x

def size(x):
    x = r(x)
    return -r(x)

x, y = 2, 3
x -= 1 
y -= 1
unite(x, y)
print(root)
x, y = 4, 3
x -= 1 
y -= 1
unite(x, y)
print(root)
x, y = 1, 3
x -= 1 
y -= 1
unite(x, y)
print(root)
