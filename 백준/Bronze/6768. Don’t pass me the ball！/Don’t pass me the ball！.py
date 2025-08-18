# 6768  Don’t pass me the ball!

import math

J = int(input())

if J < 4 :
    print(0)
else :
    print(math.comb(J - 1, 3))