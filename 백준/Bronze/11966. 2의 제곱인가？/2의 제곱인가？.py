# 11966 2의 제곱인가?

flag = 0 
N = int(input())
s = bin(N)[2 : ]
for i in range(1, len(s)) :
    if s[i] == '1' :
        flag = 1
        print('0')
        break
if flag == 0 :
    print('1')