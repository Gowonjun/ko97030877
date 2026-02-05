# 8714  Monety

n = int(input())
h, t = 0, 0
L = list(map(int, input().split()))
for elem in L :
    if elem == 1 :
        h += 1
    else :
        t += 1
print(min(h, t))