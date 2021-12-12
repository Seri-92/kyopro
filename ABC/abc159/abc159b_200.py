s = list(input())
n = len(s)
s_0 = s[:(n-1)//2]
s_1 = s[(n+1)//2:]
if s_0 == s_0[::-1] and s_1 == s_1[::-1] and s == s[::-1]:
    print("Yes")
else:
    print("No")