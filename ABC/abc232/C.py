from itertools import permutations
def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

n, m = mi()
t = []
ao = []
for i in range(m):
    a, b = mi()
    t.append((a, b))
for i in range(m):
    c, d = mi()
    ao.append((c, d))
    
t_g = [[] for _ in range(n+1)]
for i in range(m):
    a, b = t[i]
    t_g[a].append(b)
    t_g[b].append(a)
    

P = list(permutations(list(range(1, n+1))))
for p in P:
    
    a_g = [[] for _ in range(n+1)]
    for i in range(m):
        c, d = ao[i]
        c, d = p[c-1], p[d-1]
        a_g[c].append(d)
        a_g[d].append(c)



    flag = True

    for i in range(n):
        x = set(t_g[i])
        y = set(a_g[i])
        if x != y:
            flag = False
    if flag:
        print('Yes')
        exit()

print('No')
