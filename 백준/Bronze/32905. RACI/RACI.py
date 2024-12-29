# 32905 RACI

flag = 0
n, m = map(int, input().split())
for i in range(n) :
    s = input()
    if s.count('A') != 1 :
        flag = 1
if flag == 1 :
    print('No')
else :
    print('Yes')