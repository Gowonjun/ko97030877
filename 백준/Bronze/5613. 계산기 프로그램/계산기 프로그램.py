# 5613  계산기 프로그램

cnt = 0
while True :
    a = input()
    if a == '=' :
        break
    elif a == '+' :
        b = int(input())
        cnt += b
    elif a == '-' :
        b = int(input())
        cnt -= b
    elif a == '*' :
        b = int(input())
        cnt *= b
    elif a == '/' :
        b = int(input())
        cnt = int(cnt // b)
    else :
        cnt += int(a)

print(cnt)
        