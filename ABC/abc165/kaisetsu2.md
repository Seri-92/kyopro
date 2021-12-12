# ABC165 C Python

## [C - Many Requirements](https://atcoder.jp/contests/abc165/tasks/abc165_c)

- 少し難しめかもしれませんが、Python であれば itertools の combinations_with_replacement という関数を使うと、重複を含む組み合わせのシーケンスが作れます。

- 実装は、条件を満たすDの総和をリストに追加していき、最後に最大値をとって出力しました。数列 A を変えるごとに総和を毎回比較しても良いでしょう。

実装は↓のようになりました。

```python
from itertools import combinations_with_replacement as cbw

n, m, q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(q)]
ans = []
for seq in cbw(range(1,m+1), n):
    d_sum = 0
    for i in range(q):
        a, b, c, d = lst[i]
        a -= 1
        b -= 1
        if seq[b]-seq[a] == c:
            d_sum += d
    ans.append(d_sum)
ans = max(ans)
print(ans)
```
