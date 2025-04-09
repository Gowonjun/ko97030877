# 8932  7종 경기

T = int(input())
for _ in range(T) :
    hap = 0
    L = list(map(int, input().split()))
    hap += int(9.23076 * pow(26.7 - L[0], 1.835))
    hap += int(1.84523 * pow(L[1] - 75, 1.348))
    hap += int(56.0211 * pow(L[2] - 1.5, 1.05))
    hap += int(4.99087 * pow(42.5 - L[3], 1.81))
    hap += int(0.188807 * pow(L[4] - 210, 1.41))
    hap += int(15.9803 * pow(L[5] - 3.8, 1.04))
    hap += int(0.11193 * pow(254 - L[6], 1.88))
    print(hap)