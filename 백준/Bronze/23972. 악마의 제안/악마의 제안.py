# 23972 악마의 제안

import math

K, N = map(int, input().split())
if N == 1 :
    print(-1)
else :
    X = (K * N) // (N - 1) 
    if K % (N - 1) != 0 :
        X += 1
    print(X)