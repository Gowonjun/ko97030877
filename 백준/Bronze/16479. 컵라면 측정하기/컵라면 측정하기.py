# 16479 컵라면 측정하기

K = int(input())
D1, D2 = map(int, input().split())
D = abs((D2 - D1)) / 2
print(pow(K, 2) - pow(D, 2))