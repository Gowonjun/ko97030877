N, H = map(int, input().split())
if N == 1 :
    n = int(input())
    if H >= n :
        print(1)
    else :
        print(0)
else :
    L = list(map(int, input().split()))
    cnt = 0
    for elem in L :
        if elem <= H :
            cnt += 1
    print(cnt)