n = input()
l = len(n)
hanbun = l // 2
if l % 2 == 1:
    print(10 ** hanbun - 1)
else:
    n_l = int(n[:hanbun])
    n_r = int(n[hanbun:])
    if n_l > n_r:
        print(n_l-1)
    else:
        print(n_l)