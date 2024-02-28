N = int(input())

cnt = 1
n = 1
d = 0

while True :
    if N <= n :
       print(cnt)
       break
    else :
        d = cnt * 6
        cnt += 1
        n += d