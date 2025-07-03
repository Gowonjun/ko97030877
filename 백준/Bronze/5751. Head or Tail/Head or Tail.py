# 5751  Head or Tail

while True :
    N = int(input())
    if N == 0 :
        break
    cnt_J, cnt_M = 0, 0
    L = list(map(int, input().split()))
    for elem in L :
        if elem == 0 :
            cnt_M += 1
        else :
            cnt_J += 1
    print('Mary won %d times and John won %d times' % (cnt_M, cnt_J))