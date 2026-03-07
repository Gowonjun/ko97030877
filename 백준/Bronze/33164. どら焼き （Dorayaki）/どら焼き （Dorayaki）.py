# 33164 どら焼き (Dorayaki)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
hap = 0
for i in range(N) :
    for j in range(M) :
        res = (A[i] + B[j]) * max(A[i], B[j])
        hap += res
print(hap)