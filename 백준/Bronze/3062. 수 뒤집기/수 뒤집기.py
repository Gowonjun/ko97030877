# 3062  수 뒤집기

T = int(input())
for _ in range(T) :
    N = int(input())
    s = str(N)
    s_r = s[::-1]
    hap = N + int(s_r)
    hap = str(hap)
    if hap == hap[::-1] :
        print('YES')
    else :
        print('NO')