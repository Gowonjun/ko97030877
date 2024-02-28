flag = 1
L = list(map(int, input().split()))
for elem in L :
    if elem != 0 and elem != 1 :       
        print('F')
        flag = 0
        break
    else :
        continue

if flag == 1 :
    print('S')