# 17614 369

hap = 0
N = int(input())
for i in range(1, N + 1) :
    i = str(i)
    for elem in i :
        if int(elem) % 3 == 0 and int(elem) != 0 :
            hap += 1
print(hap)