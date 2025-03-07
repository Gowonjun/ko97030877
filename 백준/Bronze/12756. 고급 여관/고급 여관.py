# 12756 고급 여관

AA, AL = map(int, input().split())
BA, BL = map(int, input().split())
while True :
    BL -= AA
    AL -= BA
    if AL <= 0 :
        if BL <= 0 :
            print('DRAW')
            break
        else :
            print('PLAYER B')
            break
    elif BL <= 0 :
        print('PLAYER A')
        break