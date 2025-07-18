# 1225  이상한 곱셈
# 백업

A, B = input().split()

hap = 0
for a in A :
    for b in B :
        hap += int(a) * int(b)
print(hap)