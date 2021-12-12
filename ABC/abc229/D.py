s = list(input())
k = int(input())

l = len(s)

sum_s = [0]
if s[0] == 'X':
    sum_s.append(1)
else:
    sum_s.append(0)
for i in range(1, l):
    if s[i] == 'X':
        sum_s.append(sum_s[-1] + 1)
    else:
        sum_s.append(sum_s[-1])

top = l
bottom = min(k, l)

if sum_s[-1] + k >= l:
    print(l)
    exit()


while top - bottom > 1:
    mid = (top + bottom) // 2
    flag = False
    for i in range(l-mid+1):
        if i == 0:
            X_num_tmp = sum_s[mid]
        else:
            X_num_tmp = sum_s[i+mid] - sum_s[i]    
        if X_num_tmp >= mid - k:
            flag = True
            break
    if flag:
        bottom = mid
    else:
        top = mid
    
print(bottom)
