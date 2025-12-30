# 25840 Sharing Birthdays

n = int(input())
L = []
for i in range(n) :
    L.append(input())
s = set(L)
print(len(s))