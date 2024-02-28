A, B, C = input().split()
a, b, c = int(A), int(B), int(C)

if a == b and b == c :
    s = 10000 + a * 1000

elif a == b or b == c or c == a :
    if a == b :
        s = 1000 + a * 100
    elif b == c :
        s = 1000 + b * 100
    else :
        s = 1000 + c * 100

else :
    if a > b :
        if a > c :
            s = a * 100
        else :
            s = c * 100
    elif b > a :
        if b > c :
            s = b * 100
        else : 
            s = c * 100   
print(s)