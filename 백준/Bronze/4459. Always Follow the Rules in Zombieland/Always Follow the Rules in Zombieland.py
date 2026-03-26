# 4459  Always Follow the Rules in Zombieland

q = int(input())
L = []
for _ in range(q) :
    L.append(input())

LL = []
r = int(input())
for _ in range(r) :
    LL.append(int(input()))

for elem in LL :
    if elem > 0 :
        try :
            print('Rule %d: %s' % (elem, L[elem - 1]))
        except :
            print('Rule %d: No such rule' % elem)
    else :
        print('Rule %d: No such rule' % elem)