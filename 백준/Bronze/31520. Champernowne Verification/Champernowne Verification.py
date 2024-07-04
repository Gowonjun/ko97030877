c = ''
s = input()
for i in range(1, 10 ** 9 + 1) :
    c = c + str(i)
    if len(s) <= len(c) :
        if s != c :
            print(-1)
            break
        else :
            print(i)
            break