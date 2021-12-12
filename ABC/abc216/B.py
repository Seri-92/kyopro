n = int(input())
list_ = []
for i in range(n):
    s, t = input().split()
    list_.append((s, t))
for i in range(n):
    for j in range(i+1, n):
        if list_[i] == list_[j]:
            print('Yes')
            exit()
print('No')