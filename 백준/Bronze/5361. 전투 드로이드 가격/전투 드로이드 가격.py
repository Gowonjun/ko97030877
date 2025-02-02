T = int(input())
for i in range(T) :
    A, B, C, D, E = map(int, input().split())
    price = A * 350.34 + B * 230.9 + C * 190.55 + D * 125.3 + E * 180.9
    print('$%.2f' % price)