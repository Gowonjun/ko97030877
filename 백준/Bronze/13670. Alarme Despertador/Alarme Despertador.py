# 13670 Alarme Despertador

while True :
    s = input()
    if s == '0 0 0 0' :
        break
    H1, M1, H2, M2 = map(int, s.split())
    t1 = H1 * 60 + M1
    t2 = H2 * 60 + M2
    if t2 < t1 :
        t2 += 60 * 24
    print(t2 - t1)