# 32801 Generalized FizzBuzz

FB, F, B = 0, 0, 0
n, a, b = map(int, input().split())
for i in range(1, n + 1) :
    if i % a == 0 and i % b == 0 :
        FB += 1
    elif i % a == 0 :
        F += 1
    elif i % b == 0 :
        B += 1
print(F, B, FB)