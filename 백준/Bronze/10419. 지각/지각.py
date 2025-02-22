# 10419 지각

T = int(input())
for _ in range(T) :
    d = int(input())
    for i in range(d + 2) :
        if i + pow(i, 2) > d :
            print(i - 1)
            break