# ABC163 (A〜C + D)

## [A - Circle Pond](https://atcoder.jp/contests/abc163/tasks/abc163_a)

これがIE（内部エラー）になってしまったんですよね。
Python では標準モジュール math に円周率が入っています。

```python
import math 
print(int(input()) * math.pi * 2)
```

## [B - Homework](https://atcoder.jp/contests/abc163/tasks/abc163_b)

sum とif文が書ければ大丈夫です。

```python
n, m = map(int, input().split())
A = list(map(int, input().split())) 
ans = sum(A)

if ans > n:
    ans = -1
else:
    ans = n - ans

print(ans)
```

## [C - management](https://atcoder.jp/contests/abc163/tasks/abc163_c)
A_i はリストとして受け取りました。それぞれの要素をカウントして出力すれば良いのですが、count メソッドを使うとO(N^2)で間に合いません。各A_iに対してその数のカウントをで増やしていけばO(N)で大丈夫です。

```python
N = int(input())
A = list(map(int, input().split()))
cnt = [0] * N
for i in A:
    cnt[i-1] += 1
for j in cnt:
    print(j)
```

## [追記]

## [D - Sum of Large Numbers](https://atcoder.jp/contests/abc163/tasks/abc163_d)

### 考察ポイント

* 10^100 + a の形の数の和を考える訳ですが、a の方は10^100より十分小さいので、違う個数の和が等しくなることはありません。

* i 個の和を考えるときその数のうち最大でないものを1増やすことで、合計が1増えます。よって、最小値と最大値の間の全ての数をとることができます。

実装は難しくないでしょう。

```python
n, k = map(int, input().split())

def sum_count(x):
    return (2*n-x+1)*x//2 - x*(x-1)//2 + 1

ans = 0 
for i in range(k, n+2):
    ans += sum_count(i)
ans %= 10 ** 9 + 7

print(ans)
```