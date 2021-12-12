n = int(input())
A = list(map(int, input().split()))
def f(x):
    return sum([(a_i-x)**2 for a_i in A])
print(min([f(x) for x in range(-100, 101)]))