N = int(input())
s = input()
cnt = 0
flag = 0
for i in range(N) :
    if s[i] == 'o' :
        cnt += 1
    else :
        cnt = 0
    if cnt >= 3 :
        flag += 1
        break
if flag > 0 :
    print('Yes')
else :
    print('No')