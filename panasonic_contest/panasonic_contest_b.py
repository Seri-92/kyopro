h, w = map(int, input().split())
if  h == 1 or w == 1:
    ans = 1
elif h % 2 == 0:
    ans = h // 2 * w
else:
    if w % 2 == 0:
        h_a = h//2 + 1
        ans = (h_a * 2 - 1) * w//2 
    else:
        h_a = h // 2 + 1
        ans = (h_a * 2 - 1) * (w//2) + h_a

print(ans) 
            