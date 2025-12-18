# 20674 Statistics

n = int(input())
L = []
res = 1000
hap = 0
for _ in range(n) :
    L.append(int(input()))
for elem in L :
    if elem <= res :
        res = elem
    else :
        hap += elem - res
print(hap)