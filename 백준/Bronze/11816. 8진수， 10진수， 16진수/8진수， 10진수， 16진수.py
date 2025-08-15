# 11816 8진수, 10진수, 16진수

X = input()
if X[0 : 2] == '0x' :
    print(int(X[2 : ], 16))
elif X[0] == '0' :
    print(int(X[1 : ], 8))
else :
    print(int(X))