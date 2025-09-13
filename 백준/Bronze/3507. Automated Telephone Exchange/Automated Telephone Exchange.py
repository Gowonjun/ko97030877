# 3507  Automated Telephone Exchange

n = int(input())
if n >= 199 :
    print(0)
else :
    if n >= 99 :
        print(199 - n)
    else :
        print(n + 1)