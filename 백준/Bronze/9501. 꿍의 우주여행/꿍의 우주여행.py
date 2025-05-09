# 9501  꿍의 우주여행

T = int(input())
for _ in range(T) :
    cnt = 0
    N, D = map(int, input().split())
    for _ in range(N) :
        v, f, c = map(int, input().split())
        if v * f / c >= D :
            cnt += 1
    print(cnt)