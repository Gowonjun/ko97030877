# 25801 Odd/Even Strings

s = input()
ss = ''.join(set(s))
#print(ss)
L = []
for elem in ss :
    L.append(s.count(elem))
for i in range(len(L)) :
    L[i] = L[i] % 2
#print(L)
for i in range(len(L)) :
    L[i] = str(L[i])
a = set(L)
res = ''.join(a)
#print(res)
if res == '1' :
    print(1)
elif res == '0' :
    print(0)
else :
    print('0/1')