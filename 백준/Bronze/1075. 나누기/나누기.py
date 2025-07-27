# 1075  나누기

N = int(input())
F = int(input())
ss = str(N)
N = int(ss[:-2] + '00')
while True :
    ss = str(N)
    #print(ss)
    bb = ss[-2] + ss[-1]
    b = int(bb)
    #print(b)
    a = N % F
    #print(a)
    if a == 0 :
        print(bb)
        break
    N += 1
    #print(N)