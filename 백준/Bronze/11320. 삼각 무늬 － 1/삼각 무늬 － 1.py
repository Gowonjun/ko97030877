# 11320 삼각 무늬 - 1

T = int(input())
for _ in range(T) :
    A, B = map(int, input().split())
    print(pow(int(A / B), 2))