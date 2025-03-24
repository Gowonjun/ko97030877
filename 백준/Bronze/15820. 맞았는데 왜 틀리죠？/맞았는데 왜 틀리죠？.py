# 15820 맞았는데 왜 틀리죠?

S1, S2 = map(int, input().split())
for _ in range(S1) :
    a, b = map(int, input().split())
    if a != b :
        print("Wrong Answer")
        break
else :
    for _ in range(S2) :
        a, b = map(int, input().split())
        if a != b :
            print("Why Wrong!!!")
            break
    else :
        print("Accepted")