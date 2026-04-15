# 16316 Baby Bites

n = int(input())
L = list(input().split())
flag = 0

for i in range(n) :
    if L[i] == str(i + 1) or L[i] == 'mumble' :
        #print(i + 1)
        continue
    else :
        flag = 1
        break
if flag == 0 :
    print('makes sense')
else :
    print('something is fishy')