# 10599 페르시아의 왕들

while True :
    s = input()
    if s == '0 0 0 0' :
        break
    else :
        a, b, c, d = map(int, s.split())
        print(c - b, d - a)