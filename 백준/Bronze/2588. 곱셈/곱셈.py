n1 = int(input())
n2 = int(input())

x1 = n2 % 10 # the units digit of n2

n3 = x1 * n1

print(n3)

x2 = int((n2 % 100) / 10)

n4 = x2 * n1

print(n4)

x3 = int(n2 / 100)

n5 = x3 * n1

print(n5)

print(n3 + 10*n4 + 100*n5)