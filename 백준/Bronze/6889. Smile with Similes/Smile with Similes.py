# 6889  Smile with Similes

n = int(input())
m = int(input())
Ln = []
Lm = []
for _ in range(n) :
    Ln.append(input())
for _ in range(m) :
    Lm.append(input())
for elem_n in Ln :
    for elem_m in Lm :
        print(elem_n, 'as', elem_m)