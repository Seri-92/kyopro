import sys

sys.setrecursionlimit(200005)
int1 = lambda x: int(x)-1
pDB = lambda *x: print(*x, end="\n", file=sys.stderr)
p2D = lambda x: print(*x, sep="\n", end="\n\n", file=sys.stderr)
def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def SI(): return sys.stdin.readline().rstrip()

# dij = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dij = [(0, 1), (-1, 0), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
inf = (1 << 63)-1
# inf = (1 << 31)-1
# md = 10**9+7
md = 998244353

def dfs(u, p):
    if u == y: return True
    for v in to[u]:
        if v == p: continue
        ans.append(v+1)
        if dfs(v, u): return True
        ans.pop()
    return False

n, x, y = LI()
x, y = x-1, y-1

to = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = LI1()
    to[u].append(v)
    to[v].append(u)

ans = [x+1]
dfs(x, -1)
print(*ans)
