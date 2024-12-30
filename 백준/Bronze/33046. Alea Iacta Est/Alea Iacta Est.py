# 33046 Alea Iacta Est

n = 2
cnt = 1
for i in range(n) :
    A, B = map(int, input().split())
    h = A + B   # h == hap
    if h % 4 == 0 :
        cnt += 3
    elif h % 4 == 1 :
        cnt += 0
    elif h % 4 == 2 :
        cnt += 1
    else :
        cnt += 2
    #print(cnt)
res = cnt % 4
if res == 0 :
    print(4)
else :
    print(res)