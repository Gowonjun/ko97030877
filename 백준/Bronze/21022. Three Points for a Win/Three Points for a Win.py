# 21022 Three Points for a Win

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

hap = 0
for i in range(N) :
    if A[i] > B[i] :
        hap += 3
    elif A[i] == B[i] :
        hap += 1
print(hap)