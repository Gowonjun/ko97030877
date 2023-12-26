n = int(input())
for i in range(n) :
    cnt = 0
    s = input()
    num = map(int, s.split())
    L =list(num)
    if 18 in L:
            cnt += 1
    if 17 in L:
            cnt += 2
    print(s)
    if cnt == 0 :
        print('none\n')
    elif cnt == 1 :
        print('mack\n')
    elif cnt == 2 :
        print('zack\n')
    elif cnt == 3 :
        print('both\n')