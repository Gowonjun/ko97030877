# 34027 제곱 수?

import math
T = int(input())
for i in range(T) :
    N = int(input())
    if int(math.sqrt(N)) ** 2 == N :
        print(1)
    else :
        print(0)