# 15096 Batter Up

n = int(input())
L = list(map(int, input().split()))
while -1 in L :
    L.remove(-1)
print(sum(L) / len(L))