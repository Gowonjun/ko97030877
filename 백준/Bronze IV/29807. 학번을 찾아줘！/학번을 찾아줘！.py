hap = 0
T = int(input())
if T == 5 :
    a, b, c, d, e = map(int, input().split())
    if a > c :
        hap += 508 * (a - c)
    else :
        hap += 108 * (c - a)
    if b > d :
        hap += 212 * (b - d)
    else :
        hap += 305 * (d - b)
    hap += 707 * e
if T == 4 :
    a, b, c, d = map(int, input().split())
    if a > c :
        hap += 508 * (a - c)
    else :
        hap += 108 * (c - a)
    if b > d :
        hap += 212 * (b - d)
    else :
        hap += 305 * (d - b)
if T == 3 :
    a, b, c = map(int, input().split())
    if a > c :
        hap += 508 * (a - c)
    else :
        hap += 108 * (c - a)
    hap += 212 * b
if T == 2 :
    a, b = map(int, input().split())
    hap += 508 * a
    hap += 212 * b
if T == 1 :
    a = int(input())
    hap += 508 * a
hap *= 4763
print(hap)