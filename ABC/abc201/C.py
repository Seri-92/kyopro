s = list(input())
aru = 0
wakaran = 0
for i in range(10):
    if s[i] == 'o':
        aru += 1
    elif s[i] == '?':
        wakaran += 1 
if aru > 4:
    print(0)
    exit()

mitei = 4 - aru
nokori = min(mitei, wakaran)
tukau = list(range(aru))
subete = list(range(aru+wakaran))
n = len(subete)

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                koho = [subete[i], subete[j], subete[k], subete[l]]
                flag = 1
                for s in tukau:
                    if not (s in koho):
                        flag = 0
                if flag:
                    ans += 1    
print(ans)

