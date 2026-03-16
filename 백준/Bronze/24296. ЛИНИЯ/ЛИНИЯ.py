# 24296 ЛИНИЯ

N = int(input())
while True :
    if N % 2 == 0 :
        break
    else :
        N = N // 2 + 1
print(N)