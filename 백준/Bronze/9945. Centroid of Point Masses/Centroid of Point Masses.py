# 9945  Centroid of Point Masses

i = 1
while True :
    hap_x = 0
    hap_y = 0
    hap_m = 0
    n = int(input())
    if n < 0 :
        break
    for _ in range(n) :
        x, y, m = map(int, input().split())
        hap_x += x * m
        hap_y += y * m
        hap_m += m / n
    print('Case %d: %.2f %.2f' % (i, (hap_x / n) / hap_m, (hap_y / n) / hap_m))
    i += 1
    blank = input()