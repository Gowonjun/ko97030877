import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    N = int(sys.stdin.readline())
  
    
    cnt = 0

    for i in range(2, N + 1) :
        real_N = N
        while True :
            if real_N == 0 :
                break
            if real_N % i == 0 :
                cnt += 1
                real_N = real_N // i
            else :
                break
    print(cnt)