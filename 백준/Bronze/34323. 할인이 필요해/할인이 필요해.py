# 34323 할인이 필요해

N, M, S = map(int, input().split())
price_M = S * M
price_N = (100 - N) * S * (M + 1) // 100
if (100 - N) * (M + 1) > M * 100 :
    print(price_M)
else :
    print(price_N)