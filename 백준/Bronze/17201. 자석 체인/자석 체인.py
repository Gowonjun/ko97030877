flag = 0
N = int(input())
s = input()
for i in range(len(s) - 1) :
    if s[i] == s[i + 1] :
        print('No')
        flag = 1
        break
if flag == 0 :
    print('Yes')