# 34183 SUAPC 의자 준비하기

N, M, A, B = map(int, input().split())
n = (N * 3 - M)
if n <= 0 :
    print(0)
else :    
    price = n * A + B
    print(price)