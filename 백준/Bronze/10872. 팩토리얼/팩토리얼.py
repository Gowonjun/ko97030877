fact = 1
N = int(input())

if N == 0 :
        print(1)
else :    
    for i in range(N) :
        fact *= N
        N -= 1
    print(fact)