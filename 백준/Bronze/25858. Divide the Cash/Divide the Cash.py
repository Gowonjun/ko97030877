L = []
n, d = map(int, input().split())
for i in range(n) :
    num = int(input())
    L.append(num)
hap = sum(L)
unit = d / hap
for elem in L :
    print(int(unit * elem))