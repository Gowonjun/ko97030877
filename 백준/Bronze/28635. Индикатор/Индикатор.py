m = int(input())    # max
a = int(input())
b = int(input())
cnt = 0
while True :
    if a == b :
        break
    else :
        a += 1
        if a > m :
            a = 1
        cnt += 1
print(cnt)