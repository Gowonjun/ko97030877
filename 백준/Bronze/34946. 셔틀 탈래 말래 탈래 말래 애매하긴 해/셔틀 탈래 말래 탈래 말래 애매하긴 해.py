# 34946 셔틀 탈래 말래 탈래 말래 애매하긴 해

A, B, C, D = map(int, input().split())
s = A + B
w = C
if s <= D and w <= D :
    print('~.~')
elif s <= D and w > D :
    print('Shuttle')
elif s > D and w <= D :
    print('Walk')
else :
    print('T.T')