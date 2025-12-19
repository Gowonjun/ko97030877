# 19774 ABCD-код

t = int(input())
for i in range(t) :
    s = input()
    a = s[ : 2]; b = s[2 : ]
    #print(a, b)
    a = int(a)
    b = int(b)
    if (pow(a, 2) + pow(b, 2)) % 7 == 1 :
        print('YES')
    else :
        print('NO')