cnt_c = 1
cnt_b = 1
flag = 0
N, A, B = map(int, input().split())
for _ in range(N) :
    if flag == 0 :
        cnt_c += A
        cnt_b += B
        if cnt_c < cnt_b :
            flag = 1        
        elif cnt_c == cnt_b :
            cnt_b -= 1
    elif flag == 1 :
        cnt_c += B
        cnt_b += A
        if cnt_b < cnt_c :
            flag = 0        
        elif cnt_c == cnt_b :
            cnt_c -= 1
if flag == 0 :
    print(cnt_c, cnt_b)
else :
    print(cnt_b, cnt_c)