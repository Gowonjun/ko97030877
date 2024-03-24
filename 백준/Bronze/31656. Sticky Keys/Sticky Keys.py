L = []
s = input()
L = list(s)
cnt = 0
while True :
    try :
        if L[cnt] == L[cnt + 1] :
            del L[cnt]
        else :
            cnt += 1
    except :
        break
ss = ''
for elem in L :
    ss += elem
print(ss)