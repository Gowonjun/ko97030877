while True :
    s = input()
    if s == '0 0 0 0 0 0' :
        break
    L = list(map(int, s.split()))
    L.sort()
    L.pop()
    L.pop(0)
    if sum(L) % 4 == 0 :
        print(sum(L) // 4)
    else :
        print(sum(L) / 4)