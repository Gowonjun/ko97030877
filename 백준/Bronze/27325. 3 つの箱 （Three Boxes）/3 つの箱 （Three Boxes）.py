# 27325 3 つの箱 (Three Boxes)

N = int(input())
S = input()
cnt = 1
res = 0
for elem in S :
    if elem == 'L' :
        if cnt == 1 :
            pass
        else :
            cnt -= 1
    elif elem == 'R' :
        if cnt == 3 :
            pass
        else :
            cnt += 1
    if cnt == 3 :
        res += 1
print(res)