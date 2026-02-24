# 24198 Muffinspelet

N = int(input())
a, b = 0, 0
i = 0

while True :
    if N == 0 :
        break

    if N % 2 == 0 :
        res = N // 2
    else :
        res = (N // 2) + 1
        
    if i % 2 == 0 :
        b += res
    else :
        a += res
    N -= res
    i += 1
print(a, b)