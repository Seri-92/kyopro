from collections import Counter
N = int(input())
S = [input() for i in range(N)]
c = Counter(S)
ans = c.most_common()
ans = [i[0] for i in ans if i[1] == ans[0][1]]
for i in sorted(ans):
    print(i)