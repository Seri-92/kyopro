# ABC161（A〜C）

初記事。競プロ初心者です。東工大というところで学生してます。

灰色コーダーですので、あまり参考にならないと思いますが、考えたことや感想など載せていきます。output だいじ。

まあ、競プロでPython使う人は増えているようだし、Pythonの記事はまだそこまで多くない気がするので、少しは意義もあるかな。

といいつつ、コンテスト無いでACしたのはCまでです。残りは後日解けたら追記します。

##  [A - ABC Swap](https://atcoder.jp/contests/abc161/tasks/abc161_a)

箱 A, B, C の中身を入れ替えるわけですが、x、y、zの移動は簡単に追えるので、z, x, yの順番になることに気づくだけです。

```Python
x, y, z = map(int, input().split())
print(z, x, y)
```

## [B - Popular Vote](https://atcoder.jp/contests/abc161/tasks/abc161_b)

A_i をリストとして持ち、各要素が(A_i の総和) / (4M) 以上かどうかを for ループでチェックしていきました。
シンプルですね...。

``` Python
n, m = map(int, input().split())
a = list(map(int, input().split()))
popular = 0
for i in range(n):
    if a[i] >= sum(a) / (4 * m):
        popular += 1

print("Yes" if popular >= m else 'No')
```

## [C - Replacing Integer](https://atcoder.jp/contests/abc161/tasks/abc161_c)

これは少し数学力よりの問題でしょうか。
実装はめちゃ簡単です。
こういうのがすぐできたのはよかった。
絶対値とってるので少しわかりにくいかもしれませんが、結局 K を足したり引いたりした絶対値を最小にしたいので、とりあえず割り算すればいいと思います。

7 を 4 で割ったあまりは 3 ですが、これよりも |3-4|の方が小さいです（3 ≡ -1 (mod 4))。
kで割った余りは必ず0以上k未満の値として得られるので、そこからKを引いて絶対値とったもの、つまりkから余りを引いたものと比較して小さい方をとれば良いでしょう。

``` Python
n, k = map(int, input().split())
ans = min(n % k, k - (n % k))
print(ans)
```
