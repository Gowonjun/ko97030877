# 4619  루트

while True :
    B, N = map(int, input().split())
    if B == 0 and N == 0 :
        break
    i = 1
    while True :
        if B <= pow(i, N) :
            break
        i += 1
    A = i
    if abs(B - (pow(A, N))) > abs(B - (pow(A - 1, N))) :
        print(A - 1)

    else :
        print(A)