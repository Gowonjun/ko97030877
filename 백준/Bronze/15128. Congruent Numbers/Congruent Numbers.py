p1, q1, p2, q2 = map(int, input().split())

A = p1 * p2 / q1 / q2 / 2   # A = Area

if A % 1 == 0 :    
    print(1)
else :
    print(0)