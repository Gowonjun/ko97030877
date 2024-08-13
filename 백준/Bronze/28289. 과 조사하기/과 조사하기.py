soft, im, ingong, il = 0, 0, 0, 0
P = int(input())    # people
for i in range(P) :
    L = list(map(int, input().split()))
    if L[0] == 1 :
        il += 1
    else :
        if L[1] == 1 or L[1] == 2 :
            soft += 1
        elif L[1] == 3 :
            im += 1
        else :
            ingong += 1
print('%d\n%d\n%d\n%d' % (soft, im, ingong, il))