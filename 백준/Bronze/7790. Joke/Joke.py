# 7790  Joke

L = []
while True :
    try :
        s = input()
        L.append(s)
    except :
        break

cnt = 0
for elem in L :
    cnt += elem.count('joke')
print(cnt)