T = int(input())

for i in range(T) :
    n = 0
    n = int(input())
    n_ = n // 5
    r = 0   # remainder
    r = n % 5
    print('++++ ' * n_ + '|' * r)