# 5362  Garbled Message

L = []
while True :
    try :
        L.append(input())
    except :
        break
for elem in L :
    print(elem.replace('iiing', 'th'))