H, M = input().split()
h, m = int(H), int(M)

if m >= 45 :
    m -= 45
else : 
    if h == 0 :
        m += 15
        h = 23
    else :
        m += 15
        h -= 1
print(h, m)