# 14913 등차수열에서 항 번호 찾기

a, d, k = map(int, input().split())
if k - a == 0 :
    print(1)
else :
    if (k - a) % d != 0 :
        print('X')
    else :
        if ((k - a) // d) + 1 < 1 :
            print('X')
        else :
            print(((k - a) // d) + 1)