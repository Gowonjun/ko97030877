# 2975  Transactions

while True :
    s = input()
    if s == '0 W 0' :
        break
    total, a, A = map(str, s.split())   # A = amount
    total = int(total)
    A = int(A)
    if a == 'W' :
        res = total - A
    else :
        res = total + A
    if res < -200 :
        print('Not allowed')
    else :
        print(res)