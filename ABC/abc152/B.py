a, b = input().split()
a_b = a * int(b)
b_a = b * int(a)
ans = [a_b, b_a]
ans.sort()
print(ans[0])