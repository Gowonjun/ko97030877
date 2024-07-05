hap = 0
for i in range(4) :
    a, b = input().split()
    b = int(b)
    if a == 'Es' :
        hap += b * 21
    else :
        hap += b * 17
print(hap)