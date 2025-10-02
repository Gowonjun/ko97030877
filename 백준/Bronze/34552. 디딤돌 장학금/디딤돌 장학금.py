# 34552 디딤돌 장학금

hap = 0
LL = list(map(int, input().split()))
N = int(input())
for i in range(N) :
    B, L, S = input().split()
    B = int(B)
    L = float(L)
    S = int(S)
    if L >= 2 and S >= 17 :
        hap += LL[B]
print(hap)