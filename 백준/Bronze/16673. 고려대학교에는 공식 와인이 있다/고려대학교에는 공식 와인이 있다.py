# 16673 고려대학교에는 공식 와인이 있다

C, K, P = map(int, input().split())
hap = 0
for i in range(C + 1) :
    hap += K * i + P * pow(i, 2)
print(hap)