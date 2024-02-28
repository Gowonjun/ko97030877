N = int(input())
if N == 0 :
    print(1)
else :
    multi = 1
    while True :
        if N == 1 :
            break        
        multi *= N
        N -= 1
    print(multi % 10)