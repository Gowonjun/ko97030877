# 34455 Donut Shop

D = input()
E = int(input())
s = D
for i in range(E) :
    symbol = input()
    Q = input()
    s = s + symbol + Q
print(eval(s))