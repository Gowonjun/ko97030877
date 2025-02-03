# 4892  숫자 맞추기 게임

cnt = 0
while True :
    cnt += 1
    n0 = int(input())
    if n0 == 0 :
        break
    n1 = 3 * n0
    if n1 % 2 == 0 :
        flag = 'even'
        n2 = n1 // 2
    else :
        flag = 'odd'
        n2 = (n1 + 1) // 2
    n3 = 3 * n2
    n4 = n3 // 9
    print('%d. %s %d' % (cnt, flag, n4))