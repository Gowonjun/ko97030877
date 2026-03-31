# 5365  Decoder

n = int(input())
L = list(input().split())
s = ''
for i in range(n) :
    if i == 0 :
        s = s + L[i][0]
    else :
        try :
            a = L[i][len(L[i - 1]) - 1]
        except :
            a = ' '
        s = s + a
    #print(s)
print(s)