# 21105 New Financial Year

N = int(input())
for i in range(N) :
    P, C = map(float, input().split())
    print(100 * P / (C + 100))