# 13236 Collatz Conjecture

L = []
n = int(input())
L.append(n)
while n != 1 :
    if n % 2 == 0 :
        n = n // 2
        L.append(n)
    else :
        n = 3 * n + 1
        L.append(n)
for elem in L :
    print(elem, end = ' ')