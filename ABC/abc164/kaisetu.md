# ABC164 (A〜C)

## [A - Sheep and Wolves](https://atcoder.jp/contests/abc164/tasks/abc164_a)

if 文を書いて、羊の数と狼の数の大小を比較するだけです。
私は三項演算子（条件演算子）を使って書いています。

```python
s, w = map(int, input().split())
print('unsafe' if w >= s else 'safe')
```

## [B - Battle](https://atcoder.jp/contests/abc164/tasks/abc164_b)

高橋君、青木君と交互に攻撃するので、青木君の体力を高橋君の攻撃力だけ減少させ、もし体力が0以下なら'Yes'を出力して終わらせます。次に高橋君についても同じようにし、これを繰り返せば良いです。

```python
a, b, c, d = map(int, input().split())
while True:
    c -= b
    if c <= 0:
        print('Yes')
        exit()
    a -= d
    if a <= 0:
        print('No')
        exit()
```

## [C - gacha](https://atcoder.jp/contests/abc164/tasks/abc164_c)

Python ならこれはかなり簡単です。S_i を　set（集合） にすると、同じ要素は一度しか出てこないので、set の要素数をカウントするだけで済みます。

```python
n = int(input())
s = []
for i in range(n):
    s.append(input())
s = set(s)
print(len(s))
```
