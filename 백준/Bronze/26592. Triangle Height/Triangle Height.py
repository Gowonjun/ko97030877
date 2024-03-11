n = int(input())
for i in range(n) :
    a, b = map(float, input().split())
    h = a / b * 2
    print('The height of the triangle is %.2f units' % h)