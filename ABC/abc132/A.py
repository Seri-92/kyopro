s = list(input())
dict_ = dict()
for i in range(4):
    if s[i] in dict_.keys():
        dict_[s[i]] += 1
    else:
        dict_[s[i]] = 1

print('Yes' if list(dict_.values()) == [2, 2] else 'No')
