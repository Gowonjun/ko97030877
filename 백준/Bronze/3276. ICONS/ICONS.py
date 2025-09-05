# 3276  ICONS

import math

N = int(input())
res = math.sqrt(N)
a = int(res)
if pow(a, 2) == N :
    print(a, a)
else :
    if a * (a + 1) >= N :
        print(a, a + 1)
    else :
        print(a + 1, a + 1)