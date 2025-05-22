# 9469  폰 노이만

P = int(input())
for i in range(P) :
    N, D, A, B, F = map(float, input().split())
    print(int(N), D / (A + B) * F)