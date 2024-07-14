N, A, B, C, D = map(int, input().split())

if N % A == 0 :
    a = int(N / A)
else :
    a = int(N / A) + 1
if N % C == 0 :
    c = int(N / C)
else :
    c = int(N / C) + 1
Pa = a * B
Pc = c * D
if Pa > Pc :
    print(Pc)
else :
    print(Pa)