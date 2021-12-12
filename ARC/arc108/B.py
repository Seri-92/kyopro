n = int(input())
s = input()
stack = []
for c in s:
    stack.append(c)
    if stack[-3:] == ['f', 'o', 'x']:
        stack.pop()
        stack.pop()
        stack.pop()

print(len(stack))