# 23080 스키테일 암호

K = int(input())
s = input()

i = 0
while True :
    try :
        print(s[i], end = '')
        i += K
    except :
        break