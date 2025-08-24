# 1371  가장 많은 글자

s = ''
while True :
    try :
        s = s + input()
    except :
        break
L = []
for i in range(97, 123) :
    L.append(s.count(chr(i)))
m = max(L)
for j in range(len(L)) :
    if L[j] == m :
        print(chr(j + 97), end = '')