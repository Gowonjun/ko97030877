# 17884 Lost Lineup

n = int(input())
L = list(map(int, input().split()))
LL = [0] * n
LL[0] = 1
#print(LL)

for i in range(len(L)) :
    LL[L[i] + 1] = i + 2
for elem in LL :
    print(elem, end = ' ')