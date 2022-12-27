n = int(input())
d = set()
ans = []
s_list = [input() for _ in range(n)]
for i in range(n):
    s = s_list[i]
    if s not in d:
        print(i+1)
    d.add(s)


