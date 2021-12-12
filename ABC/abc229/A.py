s = input()
t = input()

if s == '#.' and t == '.#':
    ans = 'No'
elif s == '.#' and t == '#.':
    ans = 'No'
else:
    ans = 'Yes'
print(ans)