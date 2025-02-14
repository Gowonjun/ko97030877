# 9094  수학적 호기심

T = int(input())
for _ in range(T) :
    cnt = 0
    n, m = map(int, input().split())
    for a in range(1, n) :
        for b in range(a + 1, n) :
            if (pow(a, 2) + pow(b, 2) + m) % (a * b) == 0 :
                cnt += 1
    print(cnt)