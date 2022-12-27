n = int(input())
list_ = []
ans = []
for i in range(n):
    query = list(map(int, input().split()))
    remove_set = set()
    if query[0] == 1:
        a, b = query[1], query[2]
        flag = True
        for j in range(len(list_)):
            s, t = list_[j]
            if a <= s and b <= t:
                flag = False
                break
            if s <= a and t <= b:
                remove_set.add(j)

        if flag:
            list_.append((a, b))

        list_tmp = []
        for i in range(len(list_)):
            if i in remove_set:
                continue
            list_tmp.append(list_[i])
        list_ = list_tmp
    else:
        ans.append(len(list_))

for a in ans:
    print(a)
