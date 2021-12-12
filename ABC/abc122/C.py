N, Q = map(int, input().split())
S = input()
S_sum_list = [0,0]
S_sum = 0
for i in range(N-1):
    if S[i] == "A" and S[i+1] == "C":
        S_sum += 1
        S_sum_list.append(S_sum)
    else:
        S_sum_list.append(S_sum)
ans = []
for j in range(Q):
    l, r = map(int, input().split())
    ans.append(S_sum_list[r] - S_sum_list[l])

for k in range(len(ans)):
    print(ans[k])

