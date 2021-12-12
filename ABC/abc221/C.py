n = list(input())
l = len(n)
for i in range(l):
    n[i] = int(n[i])

def max_kanwa(a, b, ans):
    a.sort()
    b.sort()
    a_ = 0
    b_ = 0
    for i in range(len(a)):
        a_ += a[i] * 10**i

    for i in range(len(b)):
        b_ += b[i] * 10**i
    ans = max(ans, a_ * b_)
    return ans
a = []
b = []
ans = 0
if l in [2, 3]:
    for i in range(l):
        a = []
        b = n[:]
        a.append(n[i])
        b.remove(n[i])
        ans = max_kanwa(a, b, ans)


elif l in [4, 5]:
    for i in range(l-1):
        for j in range(i+1, l):
           a = [] 
           b = n[:]
           a.append(n[i])
           a.append(n[j])
           b.remove(n[i])
           b.remove(n[j])
           ans = max_kanwa(a, b, ans)

elif l in [6, 7]:
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                a = []
                b = n[:]
                a.append(n[i])
                a.append(n[j])
                a.append(n[k])
                b.remove(n[i])
                b.remove(n[j])
                b.remove(n[k])
                ans = max_kanwa(a, b, ans)
        
else:
    for i in range(l-3):
        for j in range(i+1, l-2):
            for k in range(j+1, l-1):
                for m in range(k+1, l):
                    a = []
                    b = n[:]
                    a.append(n[i])
                    a.append(n[j])
                    a.append(n[k])
                    a.append(n[m])
                    b.remove(n[i])
                    b.remove(n[j])
                    b.remove(n[k])
                    b.remove(n[m])
                    ans = max_kanwa(a, b, ans)
           
print(ans)