# 15813 너의 이름은 몇 점이니?

res = 0
n = int(input())
s = input()
for elem in s :
    res += ord(elem) - 64
print(res)