# 28637 Смена стиля

n = int(input())
for _ in range(n) :
    s = input()
    res = ''
    for i in range(len(s)) :
        if s[i].islower() == True :
            res = res + s[i]
        else :
            res = res + '_' + s[i].lower()
    if res[0] == '_' :
        res = res[1 : ]
    print(res)