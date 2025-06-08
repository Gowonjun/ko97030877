# 25285 심준의 병역판정검사

T = int(input())
for i in range(T) :
    h, w = map(int, input().split())
    BMI = w / pow(h, 2) * 10000
    if h < 140.1 :
        print(6)
    elif h < 146 :
        print(5)
    elif h < 159 :
        print(4)
    elif h < 161 :
        if 16 < BMI and BMI < 35 :
            print(3)
        else :
            print(4)
    elif h < 204 :
        if 20 <= BMI and BMI < 25 :
            print(1)
        elif 18.5 <= BMI and BMI < 30 :
            print(2)
        elif 16 <= BMI and BMI < 35 :
            print(3)
        else :
            print(4)
    else :
        print(4)
    #print('BMI :', BMI)