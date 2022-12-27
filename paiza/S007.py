from collections import defaultdict

s = list(input())
numbers = list(map(lambda x: str(x), set(range(10))))

brackets = {'(', ')'}
dict_ = defaultdict(int)

num_tmp_s = ''
num_tmp = 1
num_list_tmp = []
for c in s:
    if c in numbers:
        num_tmp_s += c
    elif c == '(':
        num_list_tmp.append(int(num_tmp_s))
        num_tmp *= int(num_tmp_s)
        num_tmp_s = ''
    elif c == ')':
        x = num_list_tmp.pop()
        num_tmp //= x
    else:
        if num_tmp_s:
            dict_[c] += num_tmp * int(num_tmp_s)
            num_tmp_s = ''
        else: dict_[c] += num_tmp

alphabets = 'abcdefghijklmnopqrstuvwxyz'

for c in alphabets:
    print(c, dict_[c])
