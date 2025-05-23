# 23348 스트릿 코딩 파이터

L = []
A, B, C = map(int, input().split())
N = int(input())
for i in range(N) :
    hap = 0
    for j in range(3) :
        a, b, c = map(int, input().split())
        hap += a * A + b * B + c * C
    L.append(hap)
print(max(L))