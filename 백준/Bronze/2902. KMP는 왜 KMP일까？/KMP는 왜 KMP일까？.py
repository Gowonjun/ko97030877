# 2902  KMP는 왜 KMP일까?

s = input()
name = s[0]
for i in range(len(s)) :
    if s[i] == '-' :
        name = name + s[i + 1]
print(name)