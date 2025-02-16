# 11586 지영 공주님의 마법 거울

N = int(input())
L = []
for i in range(N) :
    L.append(input())
K = int(input())
if K == 1 :
    for elem in L :
        print(elem)
elif K == 2 :
    for elem in L :
        print(elem[::-1])
else :
    for elem in L[::-1] :
        print(elem)