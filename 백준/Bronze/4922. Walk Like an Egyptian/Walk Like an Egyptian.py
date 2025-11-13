# 4922  Walk Like an Egyptian

while True :
    N = int(input())
    if N == 0 :
        break
    res = pow(N, 2) - (N - 1)
    print('%d => %d' % (N, res))