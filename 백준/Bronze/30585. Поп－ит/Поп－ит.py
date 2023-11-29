h, w = map(int, input().split())
n0, n1 = 0, 0
for i in range(h) :
    s = input()
    for elem in s :
        if elem == '0' :
            n0 += 1
        else :
            n1 += 1
print(min(n0, n1))