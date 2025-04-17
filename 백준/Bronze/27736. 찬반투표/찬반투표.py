# 27736 찬반투표

N = int(input())
L = list(map(int, input().split()))
#print(L.count(0))
if L.count(0) * 2 >= N :
    print('INVALID')
else :
    c = L.count(1)
    b = L.count(-1)
    if c > b :
        print('APPROVED')
    else :
        print('REJECTED')