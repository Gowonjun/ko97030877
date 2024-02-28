A = int(input())
B = int(input())
C = int(input())

s = str(A * B * C)

for i in range(10) :
    cnt = 0
    for elem in s :
        #print('elem is', elem, 'and i is', i)
        if int(elem) == i :
            cnt += 1
    print(cnt)