n, y = map(int, input().split())
for m10000 in range(n+1):
    for m5000 in range(n+1-m10000):
        m1000 = n-m10000-m5000
        if m10000*10000+m5000*5000+m1000*1000==y:
            print(m10000, m5000, m1000)
            exit(0)
print("-1 -1 -1")
