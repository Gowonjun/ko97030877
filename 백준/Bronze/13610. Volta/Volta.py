# 13610 Volta

X, Y = map(int, input().split())
cha = Y - X
if Y % cha == 0 :
    print(Y // cha)
else :
    print((Y // cha) + 1)