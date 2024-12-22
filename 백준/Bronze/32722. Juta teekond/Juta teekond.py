# 32722 Juta teekond

flag = 0
a = int(input())
if a != 1 and a != 3 :
    flag = 1
b = int(input())
if b != 6 and b != 8 :
    flag = 1
c = int(input())
if c != 2 and c != 5 :
    flag = 1
if flag == 1 :
    print('EI')
else :
    print('JAH')