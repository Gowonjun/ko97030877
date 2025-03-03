# 14568 2017 연세대학교 프로그래밍 경시대회

n = int(input())
cnt = 0
temp = n
for i in range(2, n, 2) :
    n -= i
    for a in range(n) :
        b = n - a
        if a >= b + 2 and a > 0 and b > 0 :
            cnt += 1
            #print(i, b, a)
    n = temp
print(cnt)