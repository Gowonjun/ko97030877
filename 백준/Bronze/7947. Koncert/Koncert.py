# 7947  Koncert

z = int(input())
for i in range(z) :
    hap_r = 0
    hap_g = 0
    hap_b = 0
    for _ in range(10) :
        r, g, b = map(int, input().split())
        hap_r += r
        hap_g += g
        hap_b += b
    print(int(hap_r / 10 + 0.5), int(hap_g / 10 + 0.5), int(hap_b / 10 + 0.5))