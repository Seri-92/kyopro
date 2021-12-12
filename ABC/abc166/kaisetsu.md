# ABC166 Pythton

## [A - A?C](https://atcoder.jp/contests/abc166/tasks/abc166_a)

'ABC' と 'ARC' のどちらかが与えられるので、もう一方を出力すればよいです。

```python
s = input()
if s == 'ABC':
    ans = 'ARC'
elif s == 'ARC':
    ans = 'ABC'
print(ans)
```

## [B - Trick or Treat](https://atcoder.jp/contests/abc166/tasks/abc166_b)

- Python のset( 集合 ) は競プロでもなかなか使えます。
集合は同じ要素を追加しても要素数が増えないので、数学やっている人には自然でしょうが、押さえておきましょう。

- それぞれのお菓子について、そのお菓子をもらっている人すべてを用意した集合に放り込めば、1度でもお菓子をもらっている人はその集合にはいります。なので、そこに入っていない人数を数えて終わりです。

```python
n, k = map(int, input().split())
s = set()
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
        s.add(j)
print(n - len(s))
```

## [C - Peaks](https://atcoder.jp/contests/abc166/tasks/abc166_c)

- この問題でも set を使いました。ぜひ押さえておきましょう。

- ある道が結ぶ展望台のうち、標高の低い方の展望台は絶対良い展望台ではありません。良い展望台ではない set を作って入れておきましょう。逆に、すべての道についてこれをチェックして低い方にならなかった展望台は良い展望台です。このように実装しやすいように問題を読み替えるのが大切です。

```python
n, m = map(int, input().split())
h = list(map(int, input().split()))
false_set = set()
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if h[a] == h[b]:
        false_set.add(a)
        false_set.add(b)
    elif h[a] < h[b]:
        false_set.add(a)
    else:
        false_set.add(b)
print(n-len(false_set))
```

## [D - I hate Factorization](https://atcoder.jp/contests/abc166/tasks/abc166_d)

- X が 10^9 と大きいですが、びびってはいけません。A と B はともに5乗されるので、それぞれ1000までで全探索すれば十分です。公式の解説に詳しく書いてあります。

- 気をつけるべきポイントは、どちらかは負の数かもしれないということです。しかし、A^5 + B^5 = X を満たすものを探し、Bは-1倍すると、負の数は考えなくて良いことになります。

```python
x = int(input())
for a in range(10**3):
    for b in range(10**3):
        if a**5 - b**5 == x:
            print(a, b)
            exit()
        if a**5 + b**5 == x:
            print(a, -b)
            exit()
```
