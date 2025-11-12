# 6750  Rotating letters

a = 'IOSHZXN'
flag = 0
s = input()
for elem in s :
    if elem not in a :
        flag = 1
        break
if flag == 1 :
    print('NO')
else :
    print('YES')