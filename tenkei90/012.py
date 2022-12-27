class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
def idx(r, c):
    return (r - 1) * w + c - 1

h, w = map(int, input().split())
q = int(input())

board = [[0] * w for _ in range(h)]

uf = UnionFind(h*w)

red = [0] * (h * w)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        r, c = query[1:]
        red[idx(r, c)] = 1
        if r < h:
            if red[idx(r+1, c)]:
                uf.union(idx(r+1, c), idx(r, c))
        if c < w:
            if red[idx(r, c+1)]:
                uf.union(idx(r, c+1), idx(r, c))
        if r > 1:
            if red[idx(r-1, c)]:
                uf.union(idx(r-1, c), idx(r, c))
        if c > 1:
            if red[idx(r, c-1)]:
                uf.union(idx(r, c-1), idx(r, c))
    else:
        ra, ca, rb, cb = query[1:]
        flag = True
        if uf.same(idx(ra, ca), idx(rb, cb)):
            if red[idx(ra, ca)] and red[idx(rb, cb)]:
                print('Yes')
                flag = False
        if flag:
            print('No')

    

