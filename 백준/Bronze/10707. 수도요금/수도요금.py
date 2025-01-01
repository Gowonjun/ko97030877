# 10707 수도요금

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A * P

if P <= C :
    Y = B
else :
    Y = B + (P - C) * D
print(min(X, Y))