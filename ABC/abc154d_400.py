N, K = map(int, input().split())
p = list(map(int, input().split()))
def f(n):
    return (n+1)/2
a=[]
for i in range(N-K+1):
    a.append(sum([f(p[j]) for j in range(i, i+K)]))
print(max(a))