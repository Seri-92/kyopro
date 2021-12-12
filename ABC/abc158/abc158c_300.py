import math
a, b = map(int, input().split())
a_p = math.ceil(a / 0.08)
a_q = math.floor((a+1) / 0.08)
b_p = math.ceil(b / 0.1)
b_q = math.floor((b+1) / 0.1)
if a_p <= b_p <= a_q:
    ans = b_p
elif a_q < b_p:
    ans = -1
elif b_q < a_p:
    ans = -1
else:
    ans = a_p
print(ans)