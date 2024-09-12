import math

T = int(input())
for i in range(T) :
    N, C = map(int, input().split())
    print(math.ceil(N / C))