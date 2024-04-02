L1 = []
n, m = map(int, input().split())
for i in range(n) :
    L = []
    L = list(input())
    for j in range(m) :
        if L[j] == 'W' :
            L[j] = 'B'
        elif L[j] == 'B' :
            L[j] = 'W'
    s = ''.join(L)
    L1.append(s)

blank = input()

cnt = 0
for k in range(n) :
    ss = input()
    for l in range(m) : 
        if L1[k][l] != ss[l] :
            cnt += 1
print(cnt)