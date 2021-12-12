# ABC165 D

## [D - Floor Function](https://atcoder.jp/contests/abc165/tasks/abc165_d)

- これは数学ですかね。Nが大きいので当然全探索は間に合いません。
- 手を動かして実験すると良いと思います。入力例1 で n を大きくしてみると考えやすいかもしれません。

x を 1 ずつ大きくしていくと、x が B の倍数だと、それぞれの分数がともに整数になり、全体は0になるのがわかります。また、x = B + 1  
のときは 
floor(Ax/B) = A + floor(A/B)
A × floor(x/B) =A + A × floor(1/B)
となり、全体は x = B のときの値と等しくなります。
これでB周期で繰り返すことに気付けるのではないでしょうか。

実装はないようなものですね。

```python
a, b, n = map(int, input().split())
x = min(b-1, n)
ans = (a*x)//b - a*(x//b)
print(ans)
```