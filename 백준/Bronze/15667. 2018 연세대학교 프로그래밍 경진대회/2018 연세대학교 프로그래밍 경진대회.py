# 15667 2018 연세대학교 프로그래밍 경진대회

K = 0
N = int(input())
while True :
    K += 1
    if 1 + K + pow(K, 2) == N :
        print(K)
        break