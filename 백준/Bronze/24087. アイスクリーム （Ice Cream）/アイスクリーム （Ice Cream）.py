price = 250
S = int(input())
A = int(input())
B = int(input())
h = A
if S <= A :
    print(250)
else :
    while True :
        if S > h :
            price += 100
            h += B
        else :
            break
    print(price)