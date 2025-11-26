# 9838  XMAS

n = int(input())
L = [0] * n
for i in range(1, n + 1) :
    k = int(input())
    L[k - 1] = i
for elem in L :
    print(elem)