# 10178 할로윈의 사탕

T = int(input())
for _ in range(T) :
    c, v = map(int, input().split())
    a = c // v
    b = c % v
    print('You get %d piece(s) and your dad gets %d piece(s).' % (a, b))