t1, m1, t2, m2 = map(int, input().split())

time1 = t1 * 60 + m1
time2 = t2 * 60 + m2

if time1 <= time2 :
    m = time2 - time1
    n = m // 30
else :
    time2 += 1440
    m = time2 - time1
    n = m // 30
print(m, n)