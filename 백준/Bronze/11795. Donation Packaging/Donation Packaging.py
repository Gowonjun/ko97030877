# 11795 Donation Packaging

T = int(input())
hap_a, hap_b, hap_c = 0, 0, 0
cnt = 0
for i in range(T) :
    a, b, c = map(int, input().split())
    hap_a += a
    hap_b += b
    hap_c += c
    if hap_a >= 30 and hap_b >= 30 and hap_c >= 30 :
        x = min(hap_a, hap_b, hap_c)
        hap_a -= x
        hap_b -= x
        hap_c -= x
        print(x)
    else :
        print('NO')