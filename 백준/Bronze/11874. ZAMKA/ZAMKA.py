# 11874 ZAMKA

LL = []
L = int(input())
D = int(input())
X = int(input())

for i in range(L, D + 1) :
    hap = 0
    s = str(i)
    for elem in s :
        hap += int(elem)
    if hap == X :
        LL.append(i)
print(min(LL))
print(max(LL))