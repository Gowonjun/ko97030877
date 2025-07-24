# 25756 방어율 무시 계산하기

V = 0
N = int(input())
L = list(map(int, input().split()))
for elem in L :
    V = (1 - (1 - V / 100) * (1 - elem / 100)) * 100
    print(V)