# 4493  가위 바위 보?

t = int(input())
for _ in range(t) :
    n = int(input())
    cnt1, cnt2 = 0, 0
    for _ in range(n) :
        a, b = input().split()
        if a == 'R' :
            if b == 'P' :
                cnt2 += 1
            elif b == 'S' :
                cnt1 += 1
        elif a == 'P' :
            if b == 'S' :
                cnt2 += 1
            elif b == 'R' :
                cnt1 += 1
        else :
            if b == 'R' :
                cnt2 += 1
            elif b == 'P' :
                cnt1 += 1
    if cnt1 > cnt2 :
        print('Player 1')
    elif cnt1 < cnt2 :
        print('Player 2')
    else :
        print('TIE')