# 15340 Sim Card

while True :
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break
    L = []
    L.append(a * 30 + b * 40)
    L.append(a * 35 + b * 30)
    L.append(a * 40 + b * 20)
    print(min(L))