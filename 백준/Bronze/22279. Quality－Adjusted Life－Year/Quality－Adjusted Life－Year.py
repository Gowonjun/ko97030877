# 22279 Quality-Adjusted Life-Year

hap = 0
N = int(input())
for i in range(N) :
    q, y = map(float, input().split())
    hap += q * y
print(hap)