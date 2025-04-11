# 13223 소금 폭탄

s1 = input()
s2 = input()
if s1 == s2 :
    print('24:00:00')
else :
    h1, m1, s1 = map(int, s1.split(':'))
    h2, m2, s2 = map(int, s2.split(':'))
    t1 = 3600 * h1 + 60 * m1 + s1
    t2 = 3600 * h2 + 60 * m2 + s2
    t = t2 - t1
    if t < 0 :
        t += 24 * 60 * 60

    h = t // (60 * 60)
    m = (t % (60 * 60)) // 60
    s = (t % (60 * 60)) % (60)
    print('%02d:%02d:%02d' % (h, m, s))