# 2857  FBI

length = 5
flag = 0
for i in range(length) :
    s = input()
    if 'FBI' in s :
        flag = 1
        print(i + 1)
if flag == 0 :
    print('HE GOT AWAY!')