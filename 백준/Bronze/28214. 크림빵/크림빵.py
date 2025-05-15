# 28214 크림빵

N, K, P = map(int, input().split())
L = list(map(int, input().split()))
flag = 0
cnt = 0
hap = 0
for elem in L :
    if elem == 1 :
        cnt += 1
    flag += 1
    if flag == K :
        if cnt >= P :
            hap += 1
        flag = 0
        cnt = 0
    #print(flag, cnt, hap)
print(hap)