import sys
L = []
high = 0
alpha = ''
s = input().upper()
s_list = list(set(s))
for elem in s_list :
    n = s.count(elem)
    L.append(n)
high = max(L)
num = L.index(high)
cnt = L.count(high)
if cnt == 1 :
    alpha = s_list[num]    
else :
    alpha = '?'
print(alpha)