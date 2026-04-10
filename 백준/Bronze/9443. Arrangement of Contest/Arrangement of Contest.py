# 9443  Arrangement of Contest

n = int(input())
L = []
for _ in range(n) :
    s = input()
    c = s[0]
    a = ord(c)
    L.append(a - 64)
#print(L)
i = 1
cnt = 0
while True :
    if i > 26 :
        break
    else :
        if i in L :
            cnt += 1
        else :
            break
    i += 1
print(cnt)