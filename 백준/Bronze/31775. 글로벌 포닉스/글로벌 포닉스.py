s1 = input()
s2 = input()
s3 = input()
L = []
L.append(s1[0])
L.append(s2[0])
L.append(s3[0])
L.sort()
s = ''.join(L)
if s == 'klp' :
    print('GLOBAL')
else :
    print('PONIX')