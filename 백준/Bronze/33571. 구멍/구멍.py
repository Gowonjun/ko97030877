# 33571 구멍

hap = 0
S = input()
one = 'AabDdegOoPpQqR@'
two = 'B'
for elem in S :
    if elem in one :
        hap += 1
    elif elem in two :
        hap += 2
print(hap)