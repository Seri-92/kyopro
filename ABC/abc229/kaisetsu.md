# ABC229 A〜D Pythonによる解説

NECプログラミングコンテストとして開催されました、ABC229 の A〜D をPython で解きました。

## [A - First Grid](https://atcoder.jp/contests/abc229/tasks/abc229_a)

- 案外ミスしやすい問題な気がしました。

- 黒マスが少なくとも2つ存在することに気をつけると、「黒マスが2個で、斜めに配置されているとき」のみ黒マス同士の行き来ができません。


```Python

s = input()
t = input()

if s == '#.' and t == '.#':
    ans = 'No'
    elif s == '.#' and t == '#.':
        ans = 'No'
        else:
            ans = 'Yes'
            print(ans)
```

## [B - Hard Calculation](https://atcoder.jp/contests/abc229/tasks/abc229_b)

- 一般的な筆算の計算をイメージすれば解けます。つまり、一の位同士、十の位同士、... の和が10 以上になるかどうかをみて判定をします。

- 気をつけることは、入力をそのまま配列として受け取ると、後ろからチェックする必要があります。これは、A と B の桁数が異なる場合に位がずれてしまうからです。

```Python
a, b = input().split()
a = a[::-1]
b = b[::-1]

l = min(len(a), len(b))
for i in range(l):
    p, q = a[i], b[i]
    p = int(p)
    q = int(q)
    if p + q > 9:
        print('Hard')
        exit()
print('Easy')
```

## [C - Cheese](https://atcoder.jp/contests/abc229/tasks/abc229_c)

- 1 g あたりのおいしさが高いものから貪欲にピザにのせていけばよいです。

- $A_i$, $B_i$ をタプルなりリストなりに入れてそれをリストにぶっ込み、ソートすると良いです。デフォルトでは最初の要素でソートされます。

```Python
n, w = map(int, input().split())
list_ = []
for _ in range(n):
    list_.append(list(map(int, input().split())))

list_.sort(reverse=True)
oisisa = 0
for i in range(n):
    a, b = list_[i]
    if w == 0:
        break
    elif w >= b:
        oisisa += a * b
        w -= b
    else:
        oisisa += a * w
        w = 0
print(oisisa)
```
## [D - Longest X](https://atcoder.jp/contests/abc229/tasks/abc229_d)

- 入力例1を見てパッと見うろたえてしまいそうになりましたが、二分探索を使って何個連続させるか調べれば、間に合いそうだとわかりました。ただし、一回ごとにたくさん計算していては間に合わないので、累積和を作って、「ここからここまでに何個Xがあるか」を$\Omicron (1)$ で求められるようにしました。

- 解説見たらしゃくとり法、って書いてありました。そんなのあったな。勉強していないのでよくかりません。累積和＋二分探索で解きました。

- バグりちらかしました。

- けんちょんさんの[こちらの記事][https://qiita.com/drken/items/ecd1a472d3a0e7db8dce#3-1-%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2%E6%B3%95%E3%81%A8%E3%81%AE%E9%A1%9E%E4%BC%BC]
のよれば、しゃくとり法が想定解になっている問題は二分探索でも解けるものが多いそうです。

```Python
s = list(input())
k = int(input())

l = len(s)

sum_s = [0]
if s[0] == 'X':
    sum_s.append(1)
else:
    sum_s.append(0)
for i in range(1, l):
    if s[i] == 'X':
        sum_s.append(sum_s[-1] + 1)
    else:
        sum_s.append(sum_s[-1])

top = l
bottom = min(k, l)

if sum_s[-1] + k >= l:
    print(l)
    exit()


while top - bottom > 1:
    mid = (top + bottom) // 2
    flag = False
    for i in range(l-mid+1):
        if i == 0:
            X_num_tmp = sum_s[mid]
        else:
            X_num_tmp = sum_s[i+mid] - sum_s[i]    
        if X_num_tmp >= mid - k:
            flag = True
            break
    if flag:
        bottom = mid
    else:
        top = mid
    
print(bottom)

```

お疲れ様でした。
