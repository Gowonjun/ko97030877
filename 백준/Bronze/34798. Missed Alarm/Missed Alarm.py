# 34798 Missed Alarm

h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))
if h2 > h1 :
    print('YES')
else :
    if m2 > m1 and h2 == h1 :
        print('YES')
    else :
        print('NO')