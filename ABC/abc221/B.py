s = list(input())
t = list(input())

if s == t:
    print("Yes")
    exit()
l = len(s)
for i in range(l-1):
    s_tmp = s[:]
    s_tmp[i], s_tmp[i+1] = s_tmp[i+1], s_tmp[i]
    if s_tmp == t:
        print('Yes')
        exit()
    
print('No')