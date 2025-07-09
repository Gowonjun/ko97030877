# 2750  수 정렬하기
# 백업

L = []
N = int(input())
for i in range(N) :
    a = int(input())
    L.append(a)
L.sort()
for elem in L :
    print(elem)