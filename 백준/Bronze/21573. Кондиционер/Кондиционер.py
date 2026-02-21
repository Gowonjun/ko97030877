# 21573 Кондиционер

troom, tcond = map(int, input().split())
s = input()
if s == 'fan' :
    print(troom)
elif s == 'auto' :
    print(tcond)
else :
    if s == 'freeze' :
        if troom > tcond :
            print(tcond)
        else :
            print(troom)
    else :
        if troom < tcond :
            print(tcond)
        else :
            print(troom)