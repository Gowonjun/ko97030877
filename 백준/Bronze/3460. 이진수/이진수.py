# 3460  이진수

T = int(input())
for i in range(T) :
    n = int(input())
    bi = str(bin(n)[2 : ])
    bi = bi[::-1]
    for i in range(len(bi)) :
        if bi[i] == '1' :
            print(i, end = ' ')