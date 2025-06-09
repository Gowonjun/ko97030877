# 16504 종이접기

La = []
Lb = []
hap = 0

N = int(input())
for i in range(N) :
    a, b = map(int, input().split())
    La.append(a)
    Lb.append(b)
    if i > 0 :
        hap += abs(La[i] - La[i - 1]) + abs(Lb[i] - Lb[i - 1])
#print(La, Lb)
hap += abs(La[i] - La[0]) + abs(Lb[i] - Lb[0])
print(hap)