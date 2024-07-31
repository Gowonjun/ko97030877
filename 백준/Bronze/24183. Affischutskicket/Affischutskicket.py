C4 = 0.229 * 0.324
A3 = 0.297 * 0.42
A4 = 0.21 * 0.297

a, b, c = map(int, input().split())
print(C4 * a * 2 + A3 * b * 2 + A4 * c)