# 11312 삼각 무늬 - 2

T = int(input())
for i in range(T) :
    A, B = map(int, input().split())
    print(pow(A // B, 2))