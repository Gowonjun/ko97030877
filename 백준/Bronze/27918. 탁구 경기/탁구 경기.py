n = input()
n = int(n)

flag = 0
cnt_D = 0
cnt_P = 0
for i in range(n) :
    s = input()
    if s == 'D' :
        cnt_D += 1
    elif s == 'P' :
        cnt_P += 1
    if cnt_D >= cnt_P + 2 :
        print('%d:%d' % (cnt_D, cnt_P))
        flag = 1
        for j in range(n - cnt_D - cnt_P) :
            s = input()
        break
    elif cnt_P >= cnt_D + 2:
        print('%d:%d' % (cnt_D, cnt_P))
        flag = 1
        for j in range(n - cnt_D - cnt_P) :
            s = input()
        break
if flag == 0 :
    print('%d:%d' % (cnt_D, cnt_P))