# 14182 Tax

while True :
    n = int(input())
    if n == 0 :
        break
    if n <= 1000000 :
        pass
    elif n <= 5000000 :
        n = n - n // 10
    else :
        n = n - n // 5
    print(n)