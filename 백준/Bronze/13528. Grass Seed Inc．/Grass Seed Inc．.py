# 13528 Grass Seed Inc.

hap = 0
C = float(input())
L = int(input())
for i in range(L) :
    a, b = map(float, input().split())
    hap += a * b
print(hap * C)