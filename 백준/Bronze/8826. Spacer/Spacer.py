# 8826  Spacer

Z = int(input())
for _ in range(Z) :
    n = int(input())
    s = input()
    NS, EW = 0, 0
    for elem in s :
        if elem == 'N' :
            NS += 1
        elif elem == 'S' :
            NS -= 1
        elif elem == 'E' :
            EW += 1
        elif elem == 'W' :
            EW -= 1
    print(abs(NS) + abs(EW))