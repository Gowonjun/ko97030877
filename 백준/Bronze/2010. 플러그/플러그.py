# 2010  플러그

import sys

N = int(sys.stdin.readline())
hap = 0
# N = int(input())
for i in range(N) :
    n = int(sys.stdin.readline())
    hap += n
print(hap - N + 1)