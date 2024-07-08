La = []
Lb = []
N = int(input())
La = list(map(int, input().split()))
Lb = list(map(int, input().split()))

hap = 0
for i in range(N) :
    hap += abs(La[i] - Lb[i])

print(int(hap / 2))