hap = 0
for i in range(8) :
    s = input()
    for e in s :
        if e == 'P' :
            hap += 1
        elif e == 'p' :
            hap += -1
        elif e == 'N' :
            hap += 3
        elif e == 'n' :
            hap += -3
        elif e == 'B' :
            hap += 3
        elif e == 'b' :
            hap += -3
        elif e == 'R' :
            hap += 5
        elif e == 'r' :
            hap += -5
        elif e == 'Q' :
            hap += 9
        elif e == 'q' :
            hap += -9
print(hap)