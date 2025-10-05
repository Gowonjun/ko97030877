# 34414 Tall Enough

# 백업

flag = 0

n = int(input())

for i in range(n) :

    h = int(input())

    if h < 48 :

        flag = 1

if flag == 0 :

    print('True')

else :

    print('False')