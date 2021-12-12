s_reverse = input()[::-1]
s_reverse.replace("esare", "")
s_reverse.replace("maerd", "")
s_reverse.replace("remaerd", "")
s_reverse.replace("resare", "")
if s_reverse:
    print("No")
else:
    print("Yes")