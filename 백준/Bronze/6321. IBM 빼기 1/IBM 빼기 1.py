# 6321  IBM 빼기 1

T = int(input())
for i in range(T) :
    s = input()
    print('String #%d' % (i + 1))
    L = list(s)
    LL = []
    for elem in L :
        if elem == 'Z' :
            LL.append('A')
        else :
            elem = ord(elem) + 1
            LL.append(chr(elem))
    print(''.join(LL))
    print()