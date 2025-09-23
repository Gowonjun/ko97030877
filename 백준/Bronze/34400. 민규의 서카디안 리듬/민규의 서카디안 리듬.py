# 34400 민규의 서카디안 리듬

T = int(input())
for i in range(T) :
    t = int(input())
    t = t % 25
    if t < 17 :
        print('ONLINE')
    else :
        print('OFFLINE')