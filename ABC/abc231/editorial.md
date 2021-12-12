# ABC231 A〜D Pythonで解く

## [A - Water Pressure](https://atcoder.jp/contests/abc231/tasks/abc231_a)

- 最近A問題難しめなので身構えてしまいますが、100で割るだけです。

```Python
d = int(input())
print(d / 100)
```

## [B - Election](https://atcoder.jp/contests/abc231/tasks/abc231_b)

- 辞書を使って集計しました。

- value 最大のキーを取り出す方法がわからず、自分で書くか迷って結局ググりました。こういうロスがよくない。

```Python
n = int(input())
dict_ = dict()
for _ in range(n):
    s = input()
    if s in dict_.keys():
        dict_[s] += 1
    else:
        dict_[s] = 1

print(max(dict_, key=dict_.get)) 
```

## [C - Counting 2](https://atcoder.jp/contests/abc231/tasks/abc231_c)

- $x_j$ 以上の要素の個数を全探索で数えることができますが、これでは $\Omicron(n)$ で間に合いません。
- クエリがたくさんくる場合は、各クエリを高速で処理する必要があります。配列の順序は関係ないので、ソートしてから二分探索で処理しましょう。

- Python には bisect という標準ライブラリが使えます。ここでは、二分探索を自分で実装しています。

```Python
n, q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = []
for _ in range(q):
    x = int(input())
    if A[-1] < x:
        ans.append(0)
        continue
    ok = n - 1
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if A[mid] >= x:
            ok = mid
        else:
            ng = mid
    ans.append(n - ok)

for i in range(q):
    print(ans[i])
```

## [D - Neighbors]

- 想定とは違うかもしれないので、あとで解説を確認します。

- 2500 人も通していて、すごい...。

- 順番に条件に出てくる a と b を隣り合うようにならべていくことを考えればよいですが、すでに両隣が埋まっている、または制約に従うとループになってしまう場合を避ける必要があります。 Union Find というデータ構造を使い実装しました。ただ、Union Find だけでは解けないのでグラフも用意して隣になにが来ているかを管理しました。

- a と b を Union Find で合併していきますが、同じグループで隣ではない場合、ループになることがわかります。

```Python

from collections import defaultdict

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

n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
uf = UnionFind(n+1)
for i in range(m):
    a, b = map(int, input().split())
    if (b in G[a]) or (a in G[b]):
        continue
    if max(len(G[a]), len(G[b])) >= 2:
        print('No')
        exit()
    if uf.same(a, b):
        print('No')
        exit()
    uf.union(a, b)
    G[a].append(b)
    G[b].append(a)
    
print('Yes')
```

おつかれさまでした。
