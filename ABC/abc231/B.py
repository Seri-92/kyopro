n = int(input())
dict_ = dict()
for _ in range(n):
    s = input()
    if s in dict_.keys():
        dict_[s] += 1
    else:
        dict_[s] = 1

print(max(dict_, key=dict_.get)) 
