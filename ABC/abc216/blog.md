# ABC216 A〜C Python

## [A - Signed Difficulty](https://atcoder.jp/contests/abc216/tasks/abc216_a)

- A 問題としては少しとっつきにくかったかもしれません。

- x.y を素直に x と y で受け取ると良いでしょう。整数値のみの操作で済みます。競技プログラミングではこういうの大事です。float は極力避けるようにしておくのが無難でしょう。

- Python では、空白区切りの入力は input().split() で受け取ることができますが、split('.')とすることでドット区切りになります。カンマやコロンなども使えますね。

```python
x, y = input().split('.')
y = int(y)
if 0 <= y <= 2:
    print(x + '-')
elif 3 <= y <= 6:
    print(x)
else:
    print(x + '+')
```

## [B - Same Name](https://atcoder.jp/contests/abc216/tasks/abc216_b)

- タプル ($S_i$, $T_i$) をリストに入れていき、二重ループの全探索で同じ要素があるか調べればよいでしょう。

- $N \leq 1000$ という制約をチェックしましょう。$\Omicron (N^2)$ で通ります。

- 決して $S_i$ と $T_i$ をくっつけて一つの名前として管理してペナを出してはいけません。私です。

```python
n = int(input())
list_ = []
for i in range(n):
    s, t = input().split()
    list_.append((s, t))
for i in range(n):
    for j in range(i+1, n):
        if list_[i] == list_[j]:
            print('Yes')
            exit()
print('No')
```

## [C - Many Balls](https://atcoder.jp/contests/abc216/tasks/abc216_c)

- 先ほどまでより考察がいります。

- $N \leq 10^18$と $N$ が大きいので魔法 A ばかり使っているわけにはいかないだろうということがわかります。

- 最後の操作から逆に辿っていくことにします。例えば 14 なら偶数なら魔法 B を使って 7 → 14 と遷移できます。7は奇数なので、Bは無理。魔法 A を使い、6 → 7 と遷移できます。このように、偶数ならB, 奇数なら A と後ろから辿っていくことで最短の手順が見つかります（証明はしません）。

```python
n = int(input())
ans = []
for i in range(120):
    if n < 1:
        break
    elif n % 2 == 1:
        n -= 1
        ans.append('A')
    else: 
        n //= 2
        ans.append('B')

ans = ''.join(reversed(ans))
print(ans)
```

お疲れ様でした。