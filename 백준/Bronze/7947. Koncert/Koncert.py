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

    # 0.5를 더하고 int()로 변환하여 사사오입 구현
    avg_r = int(hap_r / 10 + 0.5)
    avg_g = int(hap_g / 10 + 0.5)
    avg_b = int(hap_b / 10 + 0.5)
    
    print(avg_r, avg_g, avg_b)