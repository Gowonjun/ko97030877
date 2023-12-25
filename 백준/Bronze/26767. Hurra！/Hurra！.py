N = int(input())

cnt = 0
for i in range(N) :
    cnt += 1
    if cnt % 77 == 0 :
        print('Wiwat!')
    elif cnt % 7 == 0 :
        print('Hurra!')
    elif cnt % 11 == 0 :
        print('Super!')
    else :
        print(cnt)