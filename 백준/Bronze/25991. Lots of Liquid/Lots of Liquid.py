L = []
n = int(input())
L = list(map(float, input().split()))
hap = 0
for elem in L :
    hap += pow(elem, 3)
res = pow(hap, 1 / 3)
print(res)