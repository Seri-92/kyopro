s = input() 
l = len(s)
q, r = divmod(l, 3)
q_2, r_2 = divmod(l-2, 3)
q_3, r_3 = divmod(l-1, 3)

unit = 'oxx'

if s[0] == 'o':
    if s == unit * q + unit[:r]:
        ans = 'Yes'
    else:
        ans = 'No'
else:
    if s == 'xx' + unit * q_2 + unit[:r_2] or \
            s == 'x' + unit * q_3 + unit[:r_3]:
        ans = 'Yes'
    else:
        ans = 'No'

print(ans)
