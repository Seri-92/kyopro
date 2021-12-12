n, k = map(int, input().split())
def f(x):
    x = list(str(x))
    N = len(x)
    g_1 = sorted(x, reverse=True)
    g_2_0 = sorted(x)
    g_2 = []
    for i in range(N):
        if g_2_0[i] != '0':
            g_2.append(g_2_0[i])
    return int(''.join(g_1)) - int(''.join(g_2))

for i in range(k):
    if n == 0:
        print(0)
        exit()
    n = f(n)

print(n)