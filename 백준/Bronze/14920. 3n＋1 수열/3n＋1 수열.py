# 14920 3n+1 수열

C = int(input())
n = 1
while True :
    if C == 1 :
        break
    if C % 2 == 0 :
        C = C / 2
    else :
        C = 3 * C + 1
    n += 1
print(n)