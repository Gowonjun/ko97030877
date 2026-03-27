# 35409 제4회 디미고 프로그래밍 챌린지

H, M = map(int, input().split())
a = H * 60 + M 
if a >= 6 * 60 + 30 and a <= 9 * 60 :
    print('Yes')
elif a >= 9 * 60 + 50 and a <= 10 * 60 :
    print('Yes')
elif a >= 10 * 60 + 50 and a <= 11 * 60 :
    print('Yes')
elif a >= 11 * 60 + 50 and a <= 12 * 60 :
    print('Yes')
elif a >= 12 * 60 + 50 and a <= 13 * 60 + 50 :
    print('Yes')
elif a >= 14 * 60 + 40 and a <= 14 * 60 + 50 :
    print('Yes')
elif a >= 15 * 60 + 40 and a <= 15 * 60 + 50 :
    print('Yes')
elif a >= 16 * 60 + 40 and a <= 22 * 60 + 50 :
    print('Yes')
else :
    print('No')