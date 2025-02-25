# 3449  해밍 거리

T = int(input())
for _ in range(T) :
    a = input()
    b = input()
    X = 0
    for i in range(len(a)) :
        if a[i] != b[i] :
            X += 1
    print('Hamming distance is %d.' % X)