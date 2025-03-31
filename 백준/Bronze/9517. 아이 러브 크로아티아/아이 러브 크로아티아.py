# 9517  아이 러브 크로아티아

t = 210 # 210s = 3m 30s
cnt = int(input())
N = int(input())
for i in range(N) :
    T, a = input().split()
    T = int(T)
    t -= T
    if t <= 0 : # t < 0
        print(cnt)
        break
    else :
        if a == 'T' :
            cnt += 1
            if cnt > 8 :
                cnt = 1