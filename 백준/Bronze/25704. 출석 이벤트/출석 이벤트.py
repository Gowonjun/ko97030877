N = int(input())
P = int(input())
res = 0
if N < 5 :
    res = P
elif N < 10 :
    res = P - 500
elif N < 15 :
    res = min(P - 500, P - (P // 10))
elif N < 20 :
    res = min(P - 2000, P - (P // 10))
else :
    res = min(P - 2000, P - (P // 4))
if res < 0 :
    print(0)
else :
    print(res)