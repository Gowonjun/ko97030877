# 2592  대표값

import statistics

N = 10
L = []
for i in range(N) :
    L.append(int(input()))
mode_value = statistics.mode(L)

print(statistics.mean(L))
print(mode_value)