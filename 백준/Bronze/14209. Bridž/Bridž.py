# 14209 Bridž

hap = 0
N = int(input())
for _ in range(N) :
    s = input()
    for elem in s :
        if elem == 'A' :
            hap += 4
        elif elem == 'K' :
            hap += 3
        elif elem == 'Q' :
            hap += 2
        elif elem == 'J' :
            hap += 1
print(hap)